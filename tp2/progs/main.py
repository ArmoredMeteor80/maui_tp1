from math import *
from outils import *


def est_supercroissante(suite: list) -> bool:
    """Renvoie Vrai si la suite est supercroissante, c-à-d que le SAD est facile"""
    somme = suite[0]
    for elt in suite[1:]:
        if somme > elt:
            return False
        somme += elt
    return True


def est_mod_acceptable(suite: list, n: int) -> bool:
    """Renvoie si le le modulo N est acceptable selon la suite"""
    somme = 0
    for elt in suite:
        somme += elt
    return n > somme


def est_compliqueur_acceptable(n: int, e: int) -> bool:
    """Renvoie si le compliqueur est acceptable selon le module"""
    return est_premier_entre_eux(e, n)


def SAD_difficile(a: list, n: int, e: int) -> list:
    """Renvoie le SAD difficile du sad facile a avec n le module et e le compliqueur"""
    return [(e * elt_a) % n for elt_a in a]


def determine_faciliteur(e: int, n: int) -> int:
    """Renvoie le facilitateur du SAD à partir de e le compliqueur et n le module"""
    return inverse_modulaire(e, n)


def dechiffrer_sad(msg: int, a: list, d: int) -> str:
    """Renvoie le message déchiffré, avec a le SAD facile et d le faciliteur"""
    # Si a est supercroissante alors on a un algo Glouton
    if est_supercroissante(a):
        msg_dechiffre = ""
        # On détermine C la capacité étant le message chiffré * le faciliteur
        c = msg*d
        n = len(a)
        for i in range(n-1, -1, -1):
            if c >= a[i]:
                c -= a[i]
                msg_dechiffre = "1" + msg_dechiffre
            else:
                msg_dechiffre = "0" + msg_dechiffre
        if c == 0:
            return msg_dechiffre
    # Sinon faire chiffre de Merkle
    return "Il n'y a pas de solution avec algo glouton"


def chiffrer_sad(msg: str, b: list, n: int) -> int:
    """Renvoie le message chiffré d'après la clé publique : SAD difficile b et le module n"""
    msg_chiffre = ""
    for i in range(0, len(msg), len(b)):
        bloc = msg[i:i+len(b)]
        bloc_chiffre = ""
        for k in range(len(bloc)):
            if int(bloc[k]) * b[k] != 0:
                bloc_chiffre += str((int(bloc[k]) * b[k]))
        msg_chiffre += bloc_chiffre
    return int(msg_chiffre) % n



if __name__ == '__main__':
    A = [93, 660, 1479, 3218, 6602, 13594]
    A2 = [2, 3, 6, 13, 27, 52]
    N = 25922
    N2 = 105
    E = 10693
    E2 = 31
    print(est_supercroissante(A2))
    print(est_mod_acceptable(A2, N2))
    print(est_compliqueur_acceptable(N2, E2))
    print(SAD_difficile(A, N, E))
    print(determine_faciliteur(E, N))
    print(f"partie publique, N : {N}, B : {SAD_difficile(A, N, E)}")
    print(dechiffrer_sad(41577, A, determine_faciliteur(E, N)))
    print(SAD_difficile(A2, N2, E2))
    print(chiffrer_sad("011000110101101110", SAD_difficile(A2, N2, E2), N2))



