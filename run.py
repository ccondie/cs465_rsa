from Crypto.Util import number
from gcd import euclid
import os

if __name__ == '__main__':
    e = 7
    p = number.getPrime(512)
    q = number.getPrime(512)
    # p = 17
    # q = 11
    n = p * q
    phi = (p - 1) * (q - 1)

    print('p:  \t' + str(p))
    print('q:  \t' + str(q))
    print('n:  \t' + str(n))
    print('phi:\t' + str(phi))

    gcd_phi_e = euclid(phi, e)
    print('gcd:\t' + str(gcd_phi_e))
