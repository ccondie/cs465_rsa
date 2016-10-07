from Crypto.Util import number
from gcd import euclid
from gcd import ext_euc_calc_d
import os

if __name__ == '__main__':
    e = 3
    # p = number.getPrime(512)
    # q = number.getPrime(512)
    p = 5
    q = 11
    n = p * q
    phi = (p - 1) * (q - 1)

    print('p:  \t' + str(p))
    print('q:  \t' + str(q))
    print('e:  \t' + str(e))
    print('n:  \t' + str(n))
    print('phi:\t' + str(phi))
    print()

    gcd_phi_e = euclid(phi, e)
    print('gcd:\t' + str(gcd_phi_e))
    print()

    d_val = ext_euc_calc_d(phi, e)

    print()
    print('d:  \t' + str(d_val))
