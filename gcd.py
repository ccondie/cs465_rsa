from modex import modex


def euclid(phi, e):
    if e == 0:
        return phi
    else:
        return euclid(e, modex(phi, 1, e))


def extended_euclid(a, b):
    pass
