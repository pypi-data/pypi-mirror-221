import math


invphi = (math.sqrt(5) - 1) / 2  # 1 / phi
invphi2 = (3 - math.sqrt(5)) / 2  # 1 / phi^2

def gss(f, a, b, tol=1e-5, thres= 0, ya=None, yb=None,fev0=0):
    """Golden section search.
    
    code taken from
    https://en.wikipedia.org/wiki/Golden-section_search

    Given a function f with a single local minimum in
    the interval [a,b], gss returns a subset interval
    [c,d] and y that contains the minimum (of value<=y) with d-c <= tol
    as well as the number fev of evaluations

    Stop as soon as an evaluation is <= thres

    Example:
    >>> f = lambda x: (x-2)**2
    >>> a = 1
    >>> b = 5
    >>> tol = 1e-5
    >>> (c,d) = gss(f, a, b, tol)
    >>> print(c, d)
    1.9999959837979107 2.0000050911830893
    """

    (a, b) = (min(a, b), max(a, b))
    h = b - a
    fev = fev0
    if ya is None:
        ya = f(a)
        fev +=1
    if yb is None:
        yb = f(b)
        fev +=1
    if min(ya,yb) <= thres or  h<=tol:
        return (a,b,min(ya,yb),fev)

    # Required steps to achieve tolerance
    n = int(math.ceil(math.log(tol / h) / math.log(invphi)))

    c = a + invphi2 * h
    d = a + invphi * h
    yc = f(c)
    yd = f(d)
    fev +=2
    if min(yc,yd) <= thres:
        return (c,d,min(yc,yd),fev)


    for k in range(n-1):
        if yc < yd:
            b = d
            d = c
            yd = yc
            h = invphi * h
            c = a + invphi2 * h
            yc = f(c)
            fev+=1
            if yc <= thres:
                return (a,b,yc,fev)
        else:
            a = c
            c = d
            yc = yd
            h = invphi * h
            d = a + invphi * h
            yd = f(d)
            fev+=1
            if yd <= thres:
                return (a,b,yd,fev)

        if ya>=yc>=yd:
            lbmin = yc + (b-c)/(d-c) * (yd-yc)
            if yb>=yd:
                xm = (c*(-b + d)*ya+(a-c) * d * yb + a * (b - d) * yc + b * (-a + c) * yd) / (-(b - d)*(ya - yc) + (a - c)*(yb - yd))
                ym = ya + (xm-a)/(c-a) * (yc-ya)
                lbmin = min(lbmin, ym)
        else:
            assert yc<=yd<=yb
            lbmin = yc - (c-a)/(d-c)*(yd-yc)
            if ya>=yc:
                xm = (c*(-b + d)*ya+(a-c) * d * yb + a * (b - d) * yc + b * (-a + c) * yd) / (-(b - d)*(ya - yc) + (a - c)*(yb - yd))
                ym = ya + (xm-a)/(c-a) * (yc-ya)
                lbmin = min(lbmin, ym)
        if lbmin >= thres + tol:
            return (a,b,lbmin,fev)


    if yc < yd:
        return (a, d, yc,fev)
    else:
        return (c, b, yd,fev)
