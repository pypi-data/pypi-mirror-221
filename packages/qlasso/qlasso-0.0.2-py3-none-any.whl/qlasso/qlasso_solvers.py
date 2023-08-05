import numpy as np
import picos
import time
import scipy.linalg as sl
import scipy.optimize as sopt
from .gss import gss

class SLassoSolver(object):
    """
    parent class of all solvers defined in this file.
    """
    def __init__(self,
                 instance,
                 tol=1e-15,
                 maxit=1000,
                 print_frequency=10,
                 screen_frequency=100,
                 optdes_crit_frequency=0,
                 screening_rules=None,
                 apply_screening=False,
                 debug=False,
                 cutoff_support=1e-20
                 ):
        """
        screening_rules is a list with elements in ['B1','B2', 'B3', 'B4', # screening rules of Pronzato & Sagnol (2021), https://hal.science/hal-02868664
                                                                           # Removing inessential points in c-and A-optimal design.
                                                                           # Journal of Statistical Planning and Inference, 213, pp.233-252.
                                                                           #
                                                    'D1', 'D2'             # new screening rules 
                                                   ]
        """

        self.instance = instance
        self.tol = tol
        self.maxit = maxit  # max number of iterations
        self.debug = debug

        # options controlling display and screen frequency
        self.print_frequency = print_frequency
        self.screen_frequency = screen_frequency
        self.optdes_crit_frequency = optdes_crit_frequency
        self.screening_rules = [] if (screening_rules is None) else screening_rules
        self.apply_screening = apply_screening

        # arrays that monitor algorithm progress
        # Following arrays are updated after each iter
        self.tab_f = []
        self.tab_support_size = []
        self.tab_pseudo_iter = []
        self.tab_time = []
        self.tab_relgap_residuals = []

        # Following arrays are updated after each "optdes_crit" iteration
        self.tab_relgap_optdes = []
        self.tab_delta_optdes = []
        # self.tab_diff_optdes = []
        self.optdes_iter = []

        # Following arrays are updated after each "screening" iteration
        self.tab_n_candidates = []
        self.screen_iter = []

        # Number of evaluations of f function for s-proc elimination
        self.fbeta_eval = 0
        self.fbeta_problems = 0

        # This table counts #features screened out -- WHEN ALL RULES WERE ACTIVATED TOGETHER IN PREVIOUS ITERS... --
        # Counting the actual rejection rate for each rule requires re-solving with single rule activated,
        # as otherwise we loose the benefit from screening.
        #
        # Alternatively, the correct rejection rates are returned whenever apply_screening is set to False,
        # but in that case we only study the rejection rate without improving the CPU
        self.screening_rejection = {rule: [] for rule in self.screening_rules}
        if not self.apply_screening:
            self.screening_candidates = {rule: list(range(self.instance.p)) for rule in self.screening_rules}

        # iteration counters
        self.pseudo_it = 0.
        self.it = 0

        # cutoff to estimate support
        self.cutoff_support = cutoff_support

        # This value might change for some algos, so init to None
        self.lbda = None

        # current iterate
        self.x = None
        self.ff = None
        self.dual_value_residuals = None
        self.relgap_residuals = np.inf
        self.relgap_optdes = np.inf
        self.support = list(range(self.instance.p))

        # candidate features
        self.candidates = list(range(self.instance.p))
        self.n_candidates = self.instance.p

        # current dual iterate
        self.theta = None

        # preprocessing
        self.fast_Mw = True
        self.preprocess_elementary_matrices = False
        if self.preprocess_elementary_matrices and self.optdes_crit_frequency:
            self.compute_elementary_matrices()
        if 'D1' in self.screening_rules or 'D2' in self.screening_rules:
            self.norms_ai2 = np.linalg.norm(self.instance.A, axis=0) ** 2

    def iter(self):
        # performs an iteration of the algorithm (this function must be overriden in child classes for each specific solver)
        pass

    def minor_iter(self, i):
        """
        minor iter relative to feature i
        """
        pass

    def print_x(self):
        assert self.x is not None
        thres = 1. / self.instance.p * 0.001
        for i, xi in enumerate(self.x):
            if abs(xi) > thres:
                print('{0}:\t{1}'.format(i, xi))
                
    def print_w(self):
        if hasattr(self, 'w'):
            w = self.w
        else:
            w = self.get_absx()
            w = w / sum(w)
        
        thres = 1. / self.instance.p * 0.001
        for i, wi in enumerate(w):
            if wi > thres:
                print('{0}:\t{1}'.format(i, wi))
        

    def print_header(self):
        print('   it\t ps-it\t support\t   Primal\t    Dual_res\trelgapres\t     Dual_OD\trelgap_OD')

    def print_iteration(self):
        return self.print_frequency and self.it % self.print_frequency == 0

    def disp(self):
        if self.print_iteration():
            line = '{0:5d}\t{1:6.1f}\t{2:4d}\t{3:.6e}\t{4:.6e}\t{5:.3e}'.format(self.it,
                                                                                self.pseudo_it,
                                                                                len(self.support),
                                                                                self.ff,
                                                                                self.dual_value_residuals,
                                                                                self.relgap_residuals)
            if self.optdes_iteration():
                line += '\t{0:.6e}\t{1:.3e}'.format(max(0, self.dual_value_optdes), self.relgap_optdes)

            print(line)

    def disp_screening(self):
        if self.print_iteration():
            line = '  screening: remaining features:{0}\t\tRejection rate by rule: '.format(self.tab_n_candidates[-1])
            for rule in self.screening_rules:
                line += '{0}:{1:.1%}\t'.format(rule, self.screening_rejection[rule][-1] / float(self.instance.p))
            print(line)

    def primal_value(self, lbda=None):
        assert self.lbda is not None or lbda is not None
        if lbda is None:
            lbda = self.lbda

        return self.primal_f() + lbda * self.primal_g()

    def primal_f(self):
        if self.instance.r == 1:
            return 0.5 * np.linalg.norm(self.get_residuals()) ** 2
        else:
            return 0.5 * np.linalg.norm(self.get_residuals(), 'fro') ** 2


    def get_residuals(self, x=None):
        if x is None:
            x = self.x
        return self.instance.A[:, self.candidates].dot(x[self.candidates]) - self.instance.c


    def get_absx(self):
        if self.instance.r == 1:
            return abs(self.x)
        else:
            return np.linalg.norm(self.x,axis=1)

    def primal_g(self):
        if self.instance.r == 1:
            return 0.5 * np.linalg.norm(self.x, 1) ** 2
        else:
            return 0.5 * np.sum(np.linalg.norm(self.x, axis=1)) ** 2

    @property
    def relgap(self):
        return min(self.relgap_residuals, self.relgap_optdes)

    def solve(self, lbda=None):

        assert self.instance.lbda is not None or lbda is not None
        if lbda is None:
            lbda = self.instance.lbda

        self.lbda = lbda
        self.ff = self.primal_value()
        self.compute_gap()

        self.t0 = time.time()
        self.print_header()
        self.disp()

        # start the iterations
        while self.it < self.maxit:


            self.iter()
            self.iter_postprocessing()  # update it, compute f, support
            self.compute_optdes_crit()
            self.compute_gap()
            self.screen()
            self.disp()
            self.update_iter_tabs()

            if self.relgap < self.tol:
                break

        return self.x

    def update_iter_tabs(self):
        self.tab_f.append(self.ff)
        self.tab_support_size.append(len(self.support))
        self.tab_pseudo_iter.append(self.pseudo_it)
        self.tab_time.append(time.time() - self.t0)
        self.tab_relgap_residuals.append(self.relgap_residuals)

    def optdes_iteration(self):
        return self.optdes_crit_frequency and self.it % self.optdes_crit_frequency == 0 and self.it > 0

    def compute_optdes_crit(self, force=False):
        if self.optdes_iteration() or force:
            c = self.instance.c
            A = self.instance.A

            # compute M(w)
            self.compute_information_matrix()

            # compute (Mw^-1 * c)
            self.Mmc = np.linalg.lstsq(self.Mw, c, rcond=None)[0]

            self.theta_optdes_over_lbda = self.Mmc

            # compute cM-c // resp. trace KM- K
            if self.instance.r == 1:
                self.cMc = c.dot(self.Mmc)
            else:
                self.cMc = c.ravel().dot(self.Mmc.ravel())

            self.dual_value_optdes = self.instance.dual_value(self.theta_optdes_over_lbda * self.lbda, self.lbda)
            self.delta_optdes = 1 - 2 * self.dual_value_optdes / (self.lbda * self.cMc)

            if self.it < self.maxit:
                self.optdes_iter.append(self.it)
                self.tab_delta_optdes.append(self.delta_optdes)

    def compute_elementary_matrices(self):
        self.HHH = []
        A = self.instance.A
        for i in range(self.instance.p):
            self.HHH.append(np.tensordot(A.T[i], A.T[i], 0))

    def compute_information_matrix(self):

        if hasattr(self, 'w'):
            w = self.w
        else:
            w = self.get_absx()
            w = w / sum(w)

        I = self.active_coords = self.candidates
        if self.fast_Mw:
            A = self.instance.A
            AI = A.T[I]
            Mw = (AI.T * w[I]).dot(AI);
            np.fill_diagonal(Mw, np.diag(Mw) + self.lbda)
        elif self.preprocess_elementary_matrices:
            Mw = np.sum([wi * Hi for wi, Hi in zip(w[I], self.HHH[I])], axis=0) + self.lbda * np.eye(self.instance.n)
        else:
            Mw = self.lbda * np.eye(self.instance.n)
            A = self.instance.A
            for i in I:
                Mw += w[i] * np.tensordot(A.T[i], A.T[i], 0)
        self.Mw = Mw

    def screen_iteration(self):
        return self.screen_frequency and self.it % self.screen_frequency == 0 and self.it > 0

    def screen(self):
        if self.screen_iteration():
            self.screening_crit = {}
            if any([rule != 'B3' for rule in self.screening_rules]):
                self.compute_screening_ATtheta()
                self.compute_screening_criterions()
            if 'B3' in self.screening_rules:
                self.compute_tstar_screening_vec()
                self.screening_crit['B3'] = 1.

            to_remove = self.do_screening()
            if self.apply_screening:
                self.screening_postprocessing(to_remove)
            self.disp_screening()

    def iter_postprocessing(self):
        self.it += 1
        if hasattr(self, 'active_coords') and self.active_coords is not None:
            self.pseudo_it += len(self.active_coords) / float(self.instance.p)
            self.active_coords = None
        else:
            self.pseudo_it += self.n_candidates / float(self.instance.p)
        self.ff = self.primal_value()
        if hasattr(self, 'absx') and hasattr(self, 'l1_norm'):
            self.support = np.where(self.absx > self.cutoff_support * self.l1_norm / float(self.instance.p))[0]
        elif hasattr(self, 'w'):
            self.support = np.where(self.w > self.cutoff_support / float(self.instance.p))[0]
        else:
            absx = abs(self.x)
            l1norm = np.sum(absx)
            self.support = np.where(absx > self.cutoff_support * l1norm / float(self.instance.p))[0]

    def screening_postprocessing(self, to_remove):
        raise NotImplementedError('necessary override in subclass')
        pass

    def screening_lhs(self, rule):
        if rule == 'D1':
            return self.screening_ATtheta_over_lbda['residuals']
        elif rule == 'B3':
            return self.tstar_screening_vec
        else:
            return self.screening_ATtheta_over_lbda['optdes']

    def do_screening(self):

        # actually filter out candidate points
        to_remove = set()
        remove_by_rule = {}

        for rule in self.screening_rules:
            rhs = self.screening_crit[rule]
            lhs = self.screening_lhs(rule)
            if rule == 'B3':
                screened = np.where(lhs < rhs)[0]
            elif self.instance.r == 1:
                screened = np.where(abs(lhs) < rhs)[0]
            else:
                screened = np.where(np.linalg.norm(lhs,axis=1) < rhs)[0]
            to_remove.update([self.candidates[i] for i in screened])
            if self.apply_screening:
                last = 0 if not (self.screening_rejection[rule]) else self.screening_rejection[rule][-1]
                self.screening_rejection[rule].append(last + len(screened))
            else:
                remove_by_rule[rule] = list(screened)

        if self.debug:
            self.old_candidates = self.candidates[:]

        self.screen_iter.append(self.it)
        if self.apply_screening:
            if self.tab_n_candidates:
                self.tab_n_candidates.append(self.tab_n_candidates[-1] - len(to_remove))
            else:
                self.tab_n_candidates.append(self.instance.p - len(to_remove))
            for i in to_remove:
                self.candidates.remove(i)
        else:
            self.tab_n_candidates.append(self.instance.p)
            for rule in self.screening_rules:
                count_rule = 0
                for i in remove_by_rule[rule]:
                    if i in self.screening_candidates[rule]:
                        count_rule += 1
                        self.screening_candidates[rule].remove(i)
                last = 0 if not (self.screening_rejection[rule]) else self.screening_rejection[rule][-1]
                self.screening_rejection[rule].append(last + count_rule)

        return to_remove

    def compute_tstar_screening_vec(self):
        if not self.optdes_iteration():
            self.compute_optdes_crit(force=True)
        th = self.Mmc
        A, c, p, n = self.instance.A, self.instance.c, self.instance.p, self.instance.n
        if self.instance.r == 1:
            tab = [((A.T[i].dot(th)) ** 2 + self.lbda * np.linalg.norm(th) ** 2) for i in range(p)]
            u = 1. / max(tab) ** 0.5 * th
            b2 = (c.dot(u)) ** 2
        else:
            tab = [(np.linalg.norm(A.T[i].dot(th)) ** 2 + self.lbda * np.linalg.norm(th,'fro') ** 2) for i in range(p)]
            u = 1. / max(tab) ** 0.5 * th
            b2 = (c.ravel().dot(u.ravel())) ** 2

        Mw = self.Mw
        iMw = np.linalg.inv(Mw)

        tstars = []
        for i0 in self.candidates:
            a = A.T[i0]
            Mma = np.linalg.inv(Mw).dot(a)
            aMa = a.dot(Mma)
            AMA = np.r_[
                np.atleast_2d(np.r_[aMa, self.lbda ** 0.5 * Mma]), np.c_[self.lbda ** 0.5 * Mma, self.lbda * iMw]]
            lb = np.linalg.norm(AMA, 2)
            H = np.tensordot(A.T[i0], A.T[i0], 0) + self.lbda * np.eye(n)
            # todo more efficient based on rank1 + identity ???
            if self.instance.r == 1:
                g = lambda x: x - b2 / c.dot(np.linalg.lstsq(x * Mw - H, c, rcond=None)[0])
            else:
                g = lambda x: x - b2 / c.ravel().dot(np.linalg.lstsq(x * Mw - H, c, rcond=None)[0].ravel())

            ts,fev = self.min_dim1(g, lb)
            tstars.append(ts)
            self.fbeta_eval += fev
            self.fbeta_problems += 1

        self.tstar_screening_vec = np.array(tstars)

    def min_dim1(self, g, lb, tol=1e-4, thres=0.):
        xx = [lb + tol]
        gg = [g(xx[-1])]
        fev = 1
        if gg[-1] <= thres:
            return gg[-1], fev
        f = 2.
        dec_found = False
        while not dec_found:
            f = (1+f)/2.
            xnew = f * xx[-1]
            gnew = g(xnew)
            fev += 1
            if gnew <= thres:
                return gnew,fev
            if f<+1+tol:
                return min(gnew,gg[0]),fev
            dec_found = gnew < gg[-1]
        xx.append(xnew)
        gg.append(gnew)
        while gg[-1] < gg[-2]:
            xx.append(f * xx[-1])
            gg.append(g(xx[-1]))
            fev += 1
            if gg[-1] <= thres:
                return gg[-1],fev

        a, b = xx[-3],xx[-1]
        ya, yb = gg[-3], gg[-1]

        xlo,xup,opt,fev = gss(g,a,b,thres=1-1e-4,tol=tol,ya=ya,yb=yb,fev0=fev)
        if self.debug:
            print(xlo,xup,opt,fev)
        return opt, fev

    def compute_screening_criterions(self):
        B1_sc, B2_sc, D1_sc, D2_sc, B4_sc = None, None, None, None, None
        if 'B1' in self.screening_rules or 'B2' in self.screening_rules:
            lmin, lmax = self.sieve_omega_eigs()
            if 'B1' in self.screening_rules:
                B1_sc = self.compute_B1_screening_crit(lmin, lmax)
            if 'B2' in self.screening_rules:
                B2_sc = self.compute_B2_screening_crit(lmin, lmax)

        if 'B4' in self.screening_rules:
            B4_sc = self.compute_B4_screening_crit()

        if 'D1' in self.screening_rules:
            D1_sc = self.compute_D1_screening_crit()

        if 'D2' in self.screening_rules:
            D2_sc = self.compute_D2_screening_crit()

        crits = {'B1': B1_sc,
                 'B2': B2_sc,
                 'D1': D1_sc,
                 'D2': D2_sc,
                 'B4': B4_sc
                 }
        self.screening_crit = crits

    def compute_B4_screening_crit(self):

        assert self.instance.r == self.instance.n
        KMmK = self.instance.c.T.dot(self.Mmc)
        eg = np.linalg.eigvalsh(KMmK)
        alpha = min(eg)/sum(eg)
        delta = self.delta_optdes

        px = lambda x: (alpha-x**2) * (1 + delta - alpha * x)**2 + (1-alpha)**3 * x**2
        sol = sopt.root_scalar(px, bracket=(alpha ** 0.5, 1))
        omega = sol.root

        # put criterion in form such that screen if abs(a'M-c) = abs(a'theta)/lbda < CR
        CR = np.maximum(0, self.cMc * omega**2/(1.+self.delta_optdes) - self.lbda * np.linalg.norm(self.Mmc,'fro')**2) ** 0.5
        return CR

    def compute_screening_ATtheta(self):
        ATtheta = {}
        if 'D1' in self.screening_rules:
            theta_residuals_over_lbda = -self.get_residuals() / self.lbda
            ATtheta['residuals'] = self.instance.A.T[self.candidates].dot(theta_residuals_over_lbda)
        if ('B1' in self.screening_rules or
                'B2' in self.screening_rules or
                'D2' in self.screening_rules or
                'B4' in self.screening_rules):
            if not self.optdes_iteration():
                self.compute_optdes_crit(force=True)
            ATtheta['optdes'] = self.instance.A.T[self.candidates].dot(self.theta_optdes_over_lbda)
        self.screening_ATtheta_over_lbda = ATtheta

    def sieve_omega_eigs(self):
        """
        compute list of Omega_i matrices and their extreme eigenvalues
        """
        A = self.instance.A

        # compute Mw^{-1/2}
        iMw = np.linalg.inv(self.Mw)
        iMh = sl.sqrtm(iMw)

        lmw = self.lbda * iMw
        Omeg = [lmw + np.tensordot(iMh.dot(A.T[i]), iMh.dot(A.T[i]), 0) for i in self.candidates]

        # compute extreme eigenvalues of each Omega_i
        lmin = []
        lmax = []
        for Oi in Omeg:
            lbi = np.linalg.eigvalsh(Oi)
            lmin.append(lbi[0])
            lmax.append(lbi[-1])

        return lmin, lmax

    def safe_radius(self, residuals=True, improved_bound=True):
        if residuals:
            delta = self.ff - self.dual_value_residuals
            R_over_lbda = (2 * delta) ** 0.5 / self.lbda
        else:
            if improved_bound:
                R_over_lbda_sq = self.delta_optdes * self.cMc / self.lbda
                R_over_lbda = R_over_lbda_sq ** 0.5

                # produces same valule as:
                # R2 = (self.instance.c.dot(self.theta_optdes_over_lbda)
                #        - 2 * self.instance.dual_value(self.theta_optdes_over_lbda* self.lbda, self.lbda) )
                # or
                # r2 = np.linalg.norm(self.theta_optdes_over_lbda * self.lbda - self.instance.c)**2 + self.lbda * ninf**2
                # R2 = self.delta_optdes/(1-self.delta_optdes) * (np.linalg.norm(self.instance.c)**2 - r2) * (1./self.lbda)
            else:
                delta = self.ff - self.instance.dual_value(self.theta_optdes_over_lbda * self.lbda, self.lbda)
                R_over_lbda = (2 * delta) ** 0.5 / self.lbda
        return R_over_lbda

    def compute_D1_screening_crit(self):
        if self.instance.r == 1:
            ninf = np.linalg.norm(self.screening_ATtheta_over_lbda['residuals'], np.inf)
        else:
            ninf = max(np.linalg.norm(self.screening_ATtheta_over_lbda['residuals'],axis=1))
        R = self.safe_radius(residuals=True)
        return ninf - R * (self.norms_ai2[self.candidates] + self.lbda) ** 0.5

    def compute_D2_screening_crit(self):
        if self.instance.r == 1:
            ninf = np.linalg.norm(self.screening_ATtheta_over_lbda['optdes'], np.inf)
        else:
            ninf = max(np.linalg.norm(self.screening_ATtheta_over_lbda['optdes'],axis=1))
        R = self.safe_radius(residuals=False, improved_bound=True)  # or improved=False
        return ninf - R * (self.norms_ai2[self.candidates] + self.lbda) ** 0.5

    def compute_B1_screening_crit(self, lmin, lmax):
        # vector of Delta (difference of extreme eigenvalues)
        Delta = np.array(lmax) - np.array(lmin)

        # delta sieve: screen out if cMHMc/cMc < crit
        crit_delta = 1 - Delta * (self.delta_optdes / (1. + self.delta_optdes)) ** 0.5

        # put criterion in form such that screen if abs(a'M-c) = abs(a'theta)/lbda < CR
        CR = np.maximum(0, self.cMc * crit_delta - self.lbda * np.linalg.norm(np.atleast_2d(self.Mmc),'fro')**2) ** 0.5
        return CR

    def compute_B2_screening_crit(self, lmin, lmax):
        # vector of kappa (ratio of extreme eigenvalues)
        kappa = np.array(lmax) / np.array(lmin)

        # delta sieve: screen out if cMHMc/cMc < crit
        phi = np.arccos(1 / (1 + self.delta_optdes) ** 0.5)
        theta = 0.5 * (phi + np.arccos((kappa - 1) / (kappa + 1) * np.cos(phi)))
        crit_kappa = (np.cos(theta - phi) ** 2 + kappa * np.sin(theta - phi) ** 2) / (
                np.cos(theta) ** 2 + kappa * np.sin(theta) ** 2)

        # put criterion in form such that screen if abs(a'M-c) = abs(a'theta)/lbda < CR
        CR = np.maximum(0, self.cMc * crit_kappa - self.lbda * np.linalg.norm(np.atleast_2d(self.Mmc), 'fro')**2) ** 0.5
        return CR

    def compute_gap(self):

        theta = -self.get_residuals()
        # self.dual_value_residuals = max(0., self.instance.dual_value(theta, self.lbda))
        self.dual_value_residuals = self.instance.dual_value(theta, self.lbda)
        self.relgap_residuals = (self.ff - self.dual_value_residuals) / self.ff

        if self.optdes_iteration():
            # self.relgap_optdes = (self.ff - max(0., self.dual_value_optdes)) / self.ff
            self.relgap_optdes = (self.ff - self.dual_value_optdes) / self.ff
            self.tab_relgap_optdes.append(self.relgap_optdes)


class PicosSolver(SLassoSolver):
    """
    SOCP-solver based on the PICOS interface for the quadratic lasso
    """
    def __init__(self, instance, tol=1e-8):
        super(PicosSolver, self).__init__(instance)
        self.tol = tol
        self.maxit = None

    def solve_primal(self, lbda=None, **options):

        t0= time.time()

        A, c, p = self.instance.A, self.instance.c, self.instance.p
        assert self.instance.lbda is not None or lbda is not None
        if lbda is None:
            lbda = self.instance.lbda

        self.lbda = lbda

        P = picos.Problem()
        x = picos.RealVariable('x', p)
        t = picos.RealVariable('t', 1)
        t2 = picos.RealVariable('t2', 1)
        l1 = picos.RealVariable('l1', 1)

        assert self.instance.r==1
        P.add_constraint(picos.Norm(A * x - c,2) <= t)
        P.add_constraint(picos.Norm(x, 1) <= l1)

        P.set_objective('min', t2)
        P.add_constraint(picos.Norm((t//(lbda**0.5 * l1)))**2 <= t2)

        t1 = time.time()
        self.picos_construction_time = t1 - t0

        self.picos_sol = P.solve(**options)
        self.x = np.array(x.value).ravel()
        self.picos_solution_time = time.time() - t1

        return self.x

    def solve_socp_jspi(self, lbda=None, **options):
        t0 = time.time()

        A, c, p, n = self.instance.A, self.instance.c, self.instance.p, self.instance.n
        assert self.instance.lbda is not None or lbda is not None
        if lbda is None:
            lbda = self.instance.lbda

        J = picos.Problem()
        u = picos.RealVariable('u', n)
        t = picos.RealVariable('t', 1)
        
        for i in range(p):
            #J.add_constraint((A.T[i] | u) ** 2 + lbda * abs(u) ** 2 <= 1)
            J += (abs( ( (A.T[i] | u) // (lbda**0.5 * t))) <= 1)
        
        J += (abs(u) <= t)
        
        J.set_objective('max', (c | u))

        t1 = time.time()
        self.picos_construction_time = t1 - t0
        self.picos_sol = J.solve(**options)

        self.u = np.array(u.value).ravel()
        self.picos_solution_time = time.time() - t1

    def solve(self, lbda=None, **options):
        self.x = self.solve_primal(lbda, **options)
        return self.x

class CDSolver(SLassoSolver):
    """
    (Block) coordinate descent, described in 
        Sagnol & Pauwels (2019). Statistical Papers 60(2):215--234
    """
    def __init__(self, instance,
                 tol=1e-8,
                 maxit=1000,
                 order='cyclic',
                 print_frequency=10,
                 screen_frequency=100,
                 optdes_crit_frequency=0,
                 screening_rules=None,
                 apply_screening=False,
                 debug=False,
                 **kwargs
                 ):
        super(CDSolver, self).__init__(instance,
                                       print_frequency=print_frequency,
                                       screen_frequency=screen_frequency,
                                       optdes_crit_frequency=optdes_crit_frequency,
                                       screening_rules=screening_rules,
                                       apply_screening=apply_screening,
                                       debug=debug)
        self.tol = tol
        self.maxit = maxit
        self.order = order

        if self.instance.r == 1:
            self.x = np.zeros(self.instance.p)
        else:
            self.x = np.zeros((self.instance.p,self.instance.r))

        if self.instance.r == 1:
            self.absx = abs(self.x)
        else:
            self.absx = np.linalg.norm(self.x,axis=1)

        self.residuals = - self.instance.c
        self.l1_norm = np.array(0.)

    def get_residuals(self):
        return self.residuals

    def get_absx(self):
        return self.absx

    def minor_iter(self, i):
        """
        One iteration of Coordinate Descent
        Operations occur INPLACE, so nothing is returned

        * `residuals` store the Ax-c
        * `absx` stores the vector (||x1||,...,||xp||)
        * `l1_norm` stores `sum(absx)`
        """
        ai = self.instance.A.T[i]
        xi = self.x[i]

        if self.absx[i]:                #absx stores |x_i| or (||x_i|| if r>1)
            if self.instance.r==1:
                self.residuals -= xi * ai
            else:
                self.residuals -= np.tensordot(ai, xi, 0)
            self.l1_norm -= self.absx[i]

        Rai = ai.dot(self.residuals)
        NRai = abs(Rai) if self.instance.r == 1 else np.linalg.norm(Rai)

        if NRai:
            delta = 1 - self.lbda * self.l1_norm / NRai
        else:
            delta = -1
        if delta > 0:
            factor = 1. / (ai.dot(ai) + self.lbda) * delta

            self.x[i] = -factor * Rai
            if self.instance.r == 1:
                self.residuals += self.x[i] * ai
                self.absx[i] = abs(self.x[i])
            else:
                self.residuals += np.tensordot(ai, self.x[i], 0)
                self.absx[i] = factor * NRai

            self.l1_norm += self.absx[i]
        else:
            self.x[i] = 0.
            self.absx[i] = 0.

    def iter(self):
        if self.order == 'cyclic':
            for i in self.candidates:
                self.minor_iter(i)
        elif self.order == 'rand':
            for i in range(self.n_candidates):
                j = self.candidates[np.random.randint(self.n_candidates)]
                self.minor_iter(j)
        elif self.order == 'randperm':
            P = np.array(self.candidates)
            np.random.shuffle(P)
            for j in P:
                self.minor_iter(j)

    def screening_postprocessing(self, to_remove):
        # zero-out points:
        for i in to_remove:
            ai = self.instance.A.T[i]
            xi = self.x[i]

            if self.instance.r == 1 :
                self.residuals -= xi * ai
                self.l1_norm -= abs(xi)
            else:
                self.residuals -= np.tensordot(ai, xi, 0)
                self.l1_norm -= np.linalg.norm(xi)
            self.absx[i] = 0.
            self.x[i] = 0.
        self.n_candidates -= len(to_remove)

class FWSolver(SLassoSolver):
    """
    Frank-Wolfe Solver. This is an implementation of the
    Fedorov-Wynn vertex-direction algorithms, adapted to the case of c- or L-optimality.
    See
        Fedorov, Theory of optimal experiments, 1972,
    or
        Wynn, The sequential design of D-optimum experimental design. Annals of Mathematical Statistics 41, 1970.
    """
    def __init__(self, instance,
                 tol=1e-8,
                 maxit=None,
                 print_frequency=10,
                 screen_frequency=100,
                 optdes_crit_frequency=0,
                 screening_rules=None,
                 apply_screening=False,
                 debug=False,
                 cutoff_support=1e-20,
                 beta=0,
                 a0=0.1,
                 ):

        super(FWSolver, self).__init__(instance,
                                                   print_frequency=print_frequency,
                                                   screen_frequency=screen_frequency,
                                                   optdes_crit_frequency=optdes_crit_frequency,
                                                   screening_rules=screening_rules,
                                                   apply_screening=apply_screening,
                                                   debug=debug,
                                                   cutoff_support=cutoff_support)
        self.tol = tol
        self.maxit = maxit
        self.beta=beta
        self.a0=a0
        
        self.w = np.ones(self.instance.p)
        self.w /= sum(self.w)

        if self.instance.r == 1:
            self.x = np.zeros(self.instance.p)
        else:
            self.x = np.zeros((self.instance.p, self.instance.r))
        
        
    def compute_optdes_diff(self):

        c = self.instance.c
        A = self.instance.A

        # compute M(w)
        if not hasattr(self,'Mw'):
            self.compute_information_matrix()

        # compute (Mw^-1 * c)
        #self.Mmc = np.linalg.lstsq(self.Mw, c, rcond=None)[0]
        #slightly faster implementation
        L = sl.cho_factor(self.Mw)
        self.Mmc = sl.cho_solve(L, c)

        self.cMmA = A.T[self.candidates].dot(self.Mmc)

        if self.instance.r == 1:
            diff = self.cMmA ** 2
        else:
            diff = np.linalg.norm(self.cMmA, axis=1) ** 2
        
        return diff

    def iter(self):
        diff = self.compute_optdes_diff()
        
        if self.instance.r == 1:#warning, there is a shift of 1 iteration for x
            self.x[self.candidates] = self.cMmA * self.w[self.candidates]
        else:
            self.x[self.candidates] = (self.cMmA.T * self.w[self.candidates]).T
            
        ii = np.argmax(diff)
        
        n = self.instance.n
        p = self.instance.p
        c = self.instance.c
        ei = np.zeros(self.n_candidates)
        ei[ii] = 1.
        
        direction = ei-self.w[self.candidates] 
        amax = 0.5
        
        alpha = min(self.a0/(1+self.it)**self.beta,amax)
        wp = self.w[self.candidates] + alpha * direction
           
        self.w[self.candidates] = self.w[self.candidates] + alpha * direction
        
        ai = self.instance.A.T[self.candidates[ii]]
        self.Mw *= (1-alpha)
        self.Mw += alpha*(np.tensordot(ai,ai,0) + self.lbda*np.eye(n))
        

    def screening_postprocessing(self, to_remove):
        # zero-out points:
        for i in to_remove:
            self.x[i] = 0.
            self.w[i] = 0.
        self.n_candidates -= len(to_remove)
  

class MultiplicativeSolver(SLassoSolver):
    """
    Multiplicative Weight Updates algortihm.
    This is a variant of the algorithm described in:
        Fellman. On the Allocation of linear observations, Comment. Phys. Math. 44:27--78, 1974.
    """
    def __init__(self, instance,
                 tol=1e-8,
                 maxit=None,
                 beta=0.5,
                 print_frequency=10,
                 screen_frequency=100,
                 optdes_crit_frequency=0,
                 screening_rules=None,
                 apply_screening=False,
                 debug=False,
                 cutoff_support=1e-20,
                 diff_wrt_H=True,
                 store_delta=False):

        super(MultiplicativeSolver, self).__init__(instance,
                                                   print_frequency=print_frequency,
                                                   screen_frequency=screen_frequency,
                                                   optdes_crit_frequency=optdes_crit_frequency,
                                                   screening_rules=screening_rules,
                                                   apply_screening=apply_screening,
                                                   debug=debug,
                                                   cutoff_support=cutoff_support)
        self.beta = beta
        self.tol = tol
        self.maxit = maxit
        self.store_delta=store_delta

        """If True, uses the diff of c'(\sum_i w_i H_i) c,where H_i = aiai' + lbda I 
        otherwise we use directly c'(\sum_i w_i aiai' + lbda I) c"""
        self.diff_wrt_H = diff_wrt_H

        self.w = np.ones(self.instance.p)
        self.w /= sum(self.w)

        if self.instance.r == 1:
            self.x = np.zeros(self.instance.p)
        else:
            self.x = np.zeros((self.instance.p, self.instance.r))

    def compute_optdes_diff(self):

        c = self.instance.c
        A = self.instance.A

        # compute M(w)
        self.compute_information_matrix()

        # compute (Mw^-1 * c)
        #self.Mmc = np.linalg.lstsq(self.Mw, c, rcond=None)[0]
        #slightly faster implementation
        L = sl.cho_factor(self.Mw)
        self.Mmc = sl.cho_solve(L, c)

        self.cMmA = A.T[self.active_coords].dot(self.Mmc)

        if self.instance.r == 1:
            diff = self.cMmA ** 2
        else:
            diff = np.linalg.norm(self.cMmA, axis=1) ** 2

        if self.diff_wrt_H:
            lmmc = self.lbda * np.linalg.norm(self.Mmc) ** 2
            return diff + lmmc
        else:
            return diff

    def compute_delta(self,diff):
        maxdif = max(diff)

        c = self.instance.c

        if self.instance.r == 1:
            self.cMc = c.dot(self.Mmc)
        else:
            self.cMc = c.ravel().dot(self.Mmc.ravel())

        if not self.diff_wrt_H:
            lmmc = self.lbda * np.linalg.norm(self.Mmc) ** 2
            maxdif += lmmc
        return maxdif/self.cMc - 1.

    def iter(self):
        diff = self.compute_optdes_diff()
        if self.store_delta:
            if not (self.optdes_iteration() or
                     (self.screen_iteration() and 'theta_optdes' in self.screening_rules)
                   ):   # otherwise delta will be computed within function compute_optdes_crit
                self.tab_delta_optdes.append(self.compute_delta(diff))
        self.w[self.active_coords] = self.w[self.active_coords] * (diff ** self.beta)
        self.w[self.active_coords] /= sum(self.w[self.active_coords])
        if self.instance.r == 1:
            self.x[self.active_coords] = self.cMmA * self.w[self.active_coords]
        else:
            self.x[self.active_coords] = (self.cMmA.T * self.w[self.active_coords]).T

    def screening_postprocessing(self, to_remove):
        # zero-out points:
        for i in to_remove:
            self.x[i] = 0.
            self.w[i] = 0.
        self.n_candidates -= len(to_remove)


class FistaSolver(SLassoSolver):
    """
    Accelerated Proximal Gradient method (Fast-Iterative Shrinkage Thresholding Algorithm) for the quadratic lasso, as described in
    Sagnol & Pauwels (2019). Statistical Papers 60(2):215--234
    """
    def __init__(self, instance,
                 tol=1e-8,
                 maxit=None,
                 print_frequency=10,
                 screen_frequency=100,
                 optdes_crit_frequency=0,
                 screening_rules=None,
                 apply_screening=False,
                 debug=False,
                 acceleration=True,
                 L0=None,  # initial estimate of Lipshitz gradient
                 reset_L_frequency=None,
                 fixed_stepsize=True
                 ):

        super(FistaSolver, self).__init__(instance,
                                          print_frequency=print_frequency,
                                          screen_frequency=screen_frequency,
                                          optdes_crit_frequency=optdes_crit_frequency,
                                          screening_rules=screening_rules,
                                          apply_screening=apply_screening,
                                          debug=debug)
        self.tol = tol
        self.maxit = maxit
        self.acceleration = acceleration
        if L0 is None:
            L0 = np.linalg.norm(instance.A, 'fro') ** 2
        self.L0 = L0
        self.L = L0
        self.reset_L_frequency = reset_L_frequency
        self.fixed_stepsize = fixed_stepsize
        if self.instance.r == 1:
            self.x = np.zeros(self.instance.p)
        else:
            self.x = np.zeros((self.instance.p,self.instance.r))
        if acceleration:
            if self.instance.r == 1:
                self.y = np.zeros(self.instance.p)
            else:
                self.y = np.zeros((self.instance.p, self.instance.r))
            self.tt = 1.
        else:
            self.y, self.tt = None, None

    @staticmethod
    def prox_g(v, t):
        """
        returns the argmin of 1/2 |x-v|_F^2 + t * (sum_i |x_i|)**2
        """
        if len(v.shape) == 1:
            p = len(v)
            r = 1
        else:
            p,r = v.shape

        if r == 1:
            nv = abs(v)
        else:
            nv = np.linalg.norm(v, axis=1)

        I = np.argsort(-nv)
        vI = v[I]
        nvI = nv[I]
        cumulative_nv = np.cumsum(nvI)

        kk = np.where([nvI[k] >= (2. * t) / (2 * t * (k + 1) + 1.) * cumulative_nv[k] for k in range(p)])[0][-1]
        alphas = [1 - (2. * t) / ((2 * t * (kk + 1) + 1.) * nvI[i]) * cumulative_nv[kk] for i in range(kk + 1)] + [
            0.] * (p - kk - 1)
        alphas = np.array(alphas)

        if r == 1:
            prox = np.zeros(p)
        else:
            prox = np.zeros((p, r))

        prox[I] = (vI.T * alphas).T
        return prox

    def proximal_gradient_line_search(self, x):
        """
        L0 is the initial estimate of the Lipschitz constant of Df
        """
        res = self.get_residuals(x)
        f_current = 0.5 * np.linalg.norm(res) ** 2

        Df = self.instance.A.T.dot(res)

        x_candidate = self.prox_g(x - 1. / self.L * Df, 0.5 * self.lbda / self.L)

        f_candidate = self.instance.primal_f(x_candidate)

        while f_candidate > f_current + Df.ravel().dot((x_candidate - x).ravel()) + self.L / 2. * np.linalg.norm(
                x_candidate - x, 'fro') ** 2:
            self.L *= 2.
            x_candidate = self.prox_g(x - 1. / self.L * Df, 0.5 * self.lbda / self.L)
            f_candidate = self.instance.primal_f(x_candidate)

        self.x = x_candidate

    def proximal_gradient_fixed_stepsize(self, x, gamma):
        Df = self.instance.A.T.dot(self.get_residuals())
        self.x = self.prox_g(x - gamma * Df, 0.5 * self.lbda * gamma)

    def iter(self):
        xm = None
        if self.fixed_stepsize:
            if self.acceleration:
                xm = np.array(self.x)
                self.proximal_gradient_fixed_stepsize(self.y, 1. / self.L)
            else:
                self.proximal_gradient_fixed_stepsize(self.x, 1. / self.L)
        else:
            if self.reset_L_frequency and self.it % self.reset_L_frequency == 0:
                self.L = self.L0

            if self.acceleration:
                xm = np.array(self.x)
                self.proximal_gradient_line_search(self.y)
            else:
                self.proximal_gradient_line_search(self.x)

        if self.acceleration:
            tp = 0.5 * (1 + (1 + 4 * self.tt ** 2) ** 0.5)
            self.y = self.x + (self.tt - 1.) / tp * (self.x - xm)
            self.tt = tp

    def screening_postprocessing(self, to_remove):
        # zero-out points:
        for i in to_remove:
            self.x[i] = 0.
        self.n_candidates -= len(to_remove)



class LarsSolver(SLassoSolver):
    """
    Adaptation of the Homotopy algorithm to solve the quadratic lasso. 
    
    The orginal algorithm for the standard (with non-squared penalty) lasso was described in
        Osborne, Presnell & Turlach (2000). IMA Journal of Numerical Analysis, 20(3):389--403.
    and 
        Efron, Hastie, Johnstone & Tibshirani (2004). The Annals of Statistics, 32(2):407--499.
    """
    
    def __init__(self, instance, tol=1e-8, maxit=None, verbose=1, debug=False, updateM=False, updateMm=False,
                 ):
        super(LarsSolver, self).__init__(instance, debug=debug)
        self.tol = tol
        self.maxit = maxit
        self.verbose = verbose
        self.updateM=updateM
        self.updateMm=updateMm
        
        
    def disp_header(self):
        if self.show_KKT_gap:
            header = 'iter\talpha\t\tlambda\t\tsupport\tKKT-gap\t\ttime'
        else:
            header = 'iter\talpha\t\tlambda\t\tsupport\ttime'
            
        print('-'*len(header.expandtabs()))
        print(header)
        print('-'*len(header.expandtabs()))
            
    def disp_homotopy(self):
        if self.show_KKT_gap:
            print(' {0}\t {1:7.5f}\t{2:8.5f}\t{3:5d}\t {4:.5e}\t {5:.3f}'.format(self.it,
                                                        self.alphas[-1],
                                                        self.lbdas[-1],
                                                        self.tab_support_size[-1],
                                                        self.KKT_gap,
                                                        self.tab_time[-1]))
        else:
            print(' {0}\t {1:7.5f}\t{2:8.5f}\t{3:5d}\t {4:.3f}'.format(self.it,
                                                        self.alphas[-1],
                                                        self.lbdas[-1],
                                                        self.tab_support_size[-1],
                                                        self.tab_time[-1]))
    
        
    def solve(self, lbda=None, show_KKT_gap=True, method=1):

        A, c, p, n = self.instance.A, self.instance.c, self.instance.p, self.instance.n
        assert self.instance.lbda is not None or lbda is not None
        if lbda is None:
            lbda = self.instance.lbda
        self.show_KKT_gap = show_KKT_gap
        self.disp_header()
            
        t0 = time.time()
            
        ATc = abs(A.T @ c)
        j = np.argmax(ATc)
        ssz = 1
        self.alphas = [ATc[j]]
        self.lbdas  = [np.inf]
        self.tab_time = [time.time()-t0]
        self.tab_support_size = [ssz]
        
        
        J = [j]
        Jb = [i for i in range(p) if i!=j]
        
        self.it = -1
        ATJ = A.T[J]
        x = np.zeros(p)
        prev_x = np.zeros(p)
        
        last_active = j
        
        if self.updateM:
            MMM = ATJ.dot(ATJ.T)
        
        while lbda < self.lbdas[self.it+1]:
            self.it += 1
            y = c-A@x
            ATJy = ATJ @ y
            if self.show_KKT_gap:
                self.KKT_gap = max(abs(abs(ATJy)-self.alphas[-1]))
            
            epJ = np.sign(ATJy)

            if not self.updateM:
                MMM = ATJ.dot(ATJ.T)            

            method = 1
            if method == 1:
                u = np.linalg.lstsq(MMM,ATc[J],rcond=-1)[0]
                v = np.linalg.lstsq(MMM,epJ,rcond=-1)[0]
            
            elif method == 2:
                if not self.updateMm:
                    MMm = np.linalg.inv(MMM)
                else:
                    raise NotImplementedError
                
                u = MMm @ ATc[J]
                v = MMm @ epJ
                
            nxt = np.zeros(p)
            with np.errstate(divide='ignore'):
                nxt[J] = np.maximum(u/v,0)
                
                z1 = A.T[Jb] @(c - ATJ.T@u)
                z2 = A.T[Jb] @ (ATJ.T@ v)
                nxt[Jb] = np.maximum(z1/(1-z2),-z1/(1+z2))
            
            nxt[last_active] = 0
            nxt[nxt > self.alphas[-1] - self.tol] = 0
            
            last_active = np.argmax(nxt)
            alpha = nxt[last_active]
                        
            self.alphas.append(alpha)
            prev_x = np.array(x)
            x = np.zeros(p)
            x[J] = u-alpha*v

            if last_active in J:
                x[last_active] = 0.
                ij = J.index(last_active)
                J.remove(last_active)
                Jb.append(last_active)
                ssz -= 1
                ATJ = np.delete(ATJ, ij, 0)
                if self.updateM:
                    Iplus = [idx for idx in range(len(J)+1) if idx != ij]
                    MMM = MMM[Iplus][:, Iplus]
            else:
                J.append(last_active)
                Jb.remove(last_active)
                ssz += 1
                if self.updateM:
                    vc = ATJ.dot(A.T[last_active])
                    nr = np.linalg.norm(A.T[last_active],2)**2
                    MMM = np.r_[np.c_[MMM, vc], np.c_[np.array([vc]), nr]]
                ATJ = A.T[J]  # seems faster than using np.r_
                
            self.lbdas.append(alpha/np.linalg.norm(x,1))
            self.tab_support_size.append(ssz)
            
            t1 = time.time()
            self.tab_time.append(t1-t0)
            self.disp_homotopy()
            
        prev_alpha = self.alphas[-2]
        
        print('--')
        
        nrm = np.linalg.norm(x,1)
        prev_nrm = np.linalg.norm(prev_x,1)
        
        denom = (prev_alpha-alpha) +  lbda * (nrm - prev_nrm)
        numer = (prev_alpha-lbda*prev_nrm)*x + (lbda*nrm-alpha)*prev_x
        self.x = numer/denom
        
        y = c-A@self.x
        ATy = A.T @ y
        
        theta = (lbda*nrm-alpha)/denom
        alpha0 = (1-theta)*alpha + theta*prev_alpha
        
        KKT_gap = abs(max(abs(ATy))-sum(abs(self.x))*lbda)
        
        if self.show_KKT_gap:
            print(' {0}\t {1:7.5f}\t{2:8.5f}\t{3:5d}\t {4:.5e}\t {5:.3f}'.format('final',
                                                        alpha0,
                                                        lbda,
                                                        ssz,
                                                        KKT_gap,
                                                        time.time()-t0))
        else:
            print(' {0}\t {1:7.5f}\t{2:8.5f}\t{3:5d}\t {4:.3f}'.format('final',
                                                        alpha0,
                                                        lbda,
                                                        ssz,
                                                        time.time()-t0))
        
        assert  KKT_gap < 1e-8
        print('optimal.')
