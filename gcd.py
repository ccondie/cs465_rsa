from modex import modex


def euclid(phi, e):
    if e == 0:
        return phi
    else:
        return euclid(e, modex(phi, 1, e))


def ext_euc_calc_d(phi_n, e):
    s = 0
    t = 1
    r = e

    old_s = 1
    old_t = 0
    old_r = phi_n

    while r != 0:
        quotient = int(old_r / r)
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    if old_t < 0:
        return phi_n + old_t
    else:
        return old_t
