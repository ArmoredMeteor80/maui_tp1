from math import *


def inverse_modulaire(a: int, n: int) -> int:
    """Renvoie l'inverse modulaire de a avec n le module"""
    r0 = a if a > n else n
    r1 = n if a > n else a
    r2 = r0 % r1
    q = r0 // r1
    u0 = 1 if a > n else 0
    u1 = 0 if a > n else 1
    u2 = u0 - u1*q
    while r2 != 0:
        r0, r1 = r1, r2
        r2 = r0 % r1
        q = r0 // r1
        u0, u1 = u1, u2
        u2 = u0 - u1*q
    return u1+n if u1 < 0 else u1


def est_premier_entre_eux(a: int, b: int) -> bool:
    """Renvoie si a et b sont premiers entre eux"""
    return gcd(a, b) == 1
