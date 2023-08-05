import numpy as np
import gzip
import struct
from .definitions import project_path

class SLassoInstance:
    def __init__(self, A, c, lbda=None):
        """
        Contain the data A,c for a Squared-Lasso instance:
            minimize 1/2 || Ax -c ||^2 + 1/2 lambda ||x||_1^2
        """
        self.A = A
        self.c = c
        self.lbda = lbda
        self.n, self.p = A.shape
        if len(self.c.shape) == 1:
            self.r = 1
            assert len(self.c) == self.n
        else:
            self.r = self.c.shape[1]
            assert self.c.shape[0] == self.n

        self._xxx = None

    @property
    def xxx(self):
        """
        localization of support points (only for `quad_reg` instances)
        """
        if self._xxx is not None:
            return self._xxx
        else:
            return np.arange(self.p)

    @classmethod
    def random_instance(cls, p, n, nnz=None, sigma=0.01, seed=None, unit=True):
        """
        Generates a random instance with a matrix A of size n (#observations) x p (#features).
        The vector c is generated as A*x+eps for a nnz-sparse vector x, where eps has noise sigma
        """
        if nnz is None:
            nnz = int(p ** 0.5) + 1

        np.random.seed(seed)
        A = np.random.randn(n, p)
        if unit:
            nA = np.linalg.norm(A, axis=0)
            A = A / nA

        x_true = np.random.randn(p)
        x_true[nnz:] = 0
        c = A.dot(x_true) + sigma * np.random.randn(n)
        if unit:
            c = c/np.linalg.norm(c)
        return cls(A, c, lbda=None)


    @classmethod
    def mnist_instance(cls, seed = None, unit=True, resize=None, sample_size=500, r=1, all_labels=False):
        import cv2 #FIXME do it here to avoid conflict

        np.random.seed(seed)

        path = project_path() + '/data/'
        train_images = path + 'train-images-idx3-ubyte.gz'
        arr_train = cls.read_idx(train_images)
        train_labels = path + 'train-labels-idx1-ubyte.gz'
        arr_labels = cls.read_idx(train_labels)
        A = []
        for i in range(10):
            target_i = np.where(arr_labels==i)[0]
            sample = np.random.choice(target_i, sample_size)
            for j in sample:
                aj = cls.prepare_image(arr_train[j], unit=unit, resize=resize)
                A.append(aj)

        test_images = path + 't10k-images-idx3-ubyte.gz'
        arr_test = cls.read_idx(test_images)

        test_labels = path + 't10k-labels-idx1-ubyte.gz'
        tst_labels = cls.read_idx(test_labels)

        jt = np.random.randint(10000)
        c = cls.prepare_image(arr_test[jt], unit=unit, resize=resize)

        A = np.array(A).T
        true_label = tst_labels[jt]
        if r%10==0 and all_labels:
            true_label=False
            K = []
            for i in range(10):
                test_i = np.where(tst_labels == i)[0]
                sample = np.random.choice(test_i, r//10)
                for j in sample:
                    aj = cls.prepare_image(arr_test[j], unit=unit, resize=resize)
                    K.append(aj)
            K = np.array(K).T
            inst = cls(A, K, lbda=None)
        elif r>1:
            test_i = np.where(tst_labels == true_label)[0]
            sample = np.random.choice(test_i, r)
            K = []
            for j in sample:
                aj = cls.prepare_image(arr_test[j], unit=unit, resize=resize)
                K.append(aj)
            K = np.array(K).T
            inst = cls(A, K, lbda=None)
        else:
            inst = cls(A, c, lbda=None)

        inst.true_label = true_label
        return inst


    @classmethod
    def quad_reg(cls, disc=201, opt_point=True, c2=0.5 * (2**0.5 - 1), degrees=None):
        if degrees is None:
            degrees = [1, 2]
        xxx = np.linspace(0, 1, disc)
        if opt_point:
            iso = np.searchsorted(xxx, (2 ** 0.5 - 1))
            xxx = np.insert(xxx, iso, (2 ** 0.5 - 1))

        A = np.array([np.array([x**d for d in degrees]) for x in xxx]).T
        c = np.array([c2 if d==2 else 1 for d in degrees])
        inst = cls(A, c, lbda=None)
        inst._xxx = xxx
        return inst


    @staticmethod
    def prepare_image(img, unit=True, resize=None):
        import cv2

        if resize:
            img = cv2.resize(img,None,fx=resize,fy=resize)
        img = img.ravel()
        if unit:
            img = img / np.linalg.norm(img)
        else:
            img = (img + 0.) / 256.
        return img


    @staticmethod
    def read_idx(filename):
        with gzip.open(filename, 'rb') as f:
            zero, data_type, dims = struct.unpack('>HBB', f.read(4))
            shape = tuple(struct.unpack('>I', f.read(4))[0] for d in range(dims))
            return np.fromstring(f.read(), dtype=np.uint8).reshape(shape)

    def primal_value(self, x, lbda=None):
        assert self.lbda is not None or lbda is not None
        if lbda is None:
            lbda = self.lbda

        return self.primal_f(x) + lbda * self.primal_g(x)

    def primal_f(self, x):
        A, c = self.A, self.c
        if self.r == 1:
            return 0.5 * np.linalg.norm(A.dot(x) - c) ** 2
        else:
            return 0.5 * np.linalg.norm(A.dot(x) - c, 'fro') ** 2


    def primal_g(self, x):
        A, c = self.A, self.c
        if self.r == 1:
            return 0.5 * np.linalg.norm(x, 1) ** 2
        else:
            return 0.5 * np.sum(np.linalg.norm(x, axis=1)) ** 2

    def dual_value(self, theta, lbda=None):
        assert self.lbda is not None or lbda is not None
        if lbda is None:
            lbda = self.lbda

        A, c = self.A, self.c
        Atheta = A.T.dot(theta)

        if self.r == 1:
            ninf = np.linalg.norm(Atheta, np.inf)
            return theta.dot(c) - 0.5 * np.linalg.norm(theta) ** 2 - 0.5 / lbda * ninf ** 2
        else:
            ninf = max(np.linalg.norm(Atheta, axis=1))
            return np.ravel(theta).dot(np.ravel(c)) - 0.5 * np.linalg.norm(theta,'fro') ** 2 - 0.5 / lbda * ninf ** 2

    def lambda_max(self):
        assert self.r == 1, "not implemented"
        A, c = self.A, self.c
        As = [A.T[i] * np.sign(A.T[i].dot(c)) for i in range(self.p)]
        gg = [ai.dot(c) for ai in As]
        i1 = np.argmax(gg)
        a1 = As[i1]
        al = [a1.dot(ai) for ai in As]
        with np.errstate(divide='ignore', invalid='ignore'):
            lmbi = [np.divide((gg[i] * al[i1] - gg[i1] * al[i]), (gg[i1] - gg[i])) for i in range(self.p)]
        lb2 = np.nanmax(lmbi)
        return lb2
