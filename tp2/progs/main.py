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


def dechiffrer_sad(msg: int, a: list, d: int, n: int) -> str:
    """Renvoie le message déchiffré, avec a le SAD facile et d le faciliteur"""
    # Si a est supercroissante alors on a un algo Glouton
    if est_supercroissante(a):
        msg_dechiffre = ""
        # On détermine C la capacité étant le message chiffré * le faciliteur
        c = (d*msg)%n
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
        bloc_chiffre = 0
        for k in range(len(bloc)):
            bloc_chiffre += int(bloc[k]) * b[k]
        print(bloc_chiffre)
        msg_chiffre += str(bloc_chiffre)
    return int(msg_chiffre)


if __name__ == '__main__':
    # Ex 1
    print("⸻⸻⸻ Ex 1 ⸻⸻⸻")
    A = [93, 660, 1479, 3218, 6602, 13594]
    print(f"est un SAD facile : {est_supercroissante(A)}")
    N = 25922
    print(f"N = {N} est module acceptable : {est_mod_acceptable(A, N)}")
    E = 10693
    print(f"E = {E} est compliqueur acceptable : {est_compliqueur_acceptable(N, E)}")
    B = SAD_difficile(A, N, E)
    print(f"le SAD diff est B = {B}")
    D = determine_faciliteur(E, N)
    print(f"Faciliteur D vaut : {D}")
    print(f"partie publique, N : {N}, B : {B}")
    print(f"partie privée, A : {A}, D :{D}")
    msg_chiffre = 41577
    msg_dechiffre = dechiffrer_sad(msg_chiffre, A, D, N)
    print(f"le msg_chiffre est {msg_chiffre} et le msg_dechiffre est {msg_dechiffre}")

    # Ex 2
    print("⸻⸻⸻ Ex 2 ⸻⸻⸻")
    A = [2, 3, 6, 13, 27, 52]
    print(f"est un SAD facile : {est_supercroissante(A)}")
    N = 105
    print(f"N = {N} est module acceptable : {est_mod_acceptable(A, N)}")
    E = 31
    print(f"E = {E} est compliqueur acceptable : {est_compliqueur_acceptable(N, E)}")
    B = SAD_difficile(A, N, E)
    print(f"le SAD diff est B = {B}")
    D = determine_faciliteur(E, N)
    print(f"Faciliteur D vaut : {D}")
    print(f"partie publique, N : {N}, B : {B}")
    print(f"partie privée, A : {A}, D :{D}")
    msg_a_chiffrer = "011000110101101110"
    msg_chiffre = chiffrer_sad(msg_a_chiffrer, B, N)
    msg_dechiffre = dechiffrer_sad(msg_chiffre, A, D, N)
    print(f"le msg_chiffre est {msg_chiffre} et le msg_dechiffre est {msg_dechiffre}")

    print()

    # ex 6 td6
    A3 = [2, 3, 17, 25, 91]
    print(f"est un SAD facile : {est_supercroissante(A3)}")
    N3 = 139
    print(f"N = {N3} est il acceptable : {est_mod_acceptable(A3, N3)}")
    E3 = 17
    print(f"E = {E3} est acceptable : {est_compliqueur_acceptable(N3, E3)}")
    B3 = SAD_difficile(A3, N3, E3)
    print(f"SAD difficile est : {B3}")
    D3 = determine_faciliteur(E3, N3)
    print(f"Faciliteur D vaut : {D3}")
    print(f"partie publique, N : {N3}, B :{B3}")
    print(f"partie privée, A : {A3}, D :{D3}")
    msg_chiffre3 = 93
    print(dechiffrer_sad(msg_chiffre3, A3, D3, N3))

    # ex de con
    A4 = [1, 3, 6]
    E4 = 7
    N4 = 12
    print(chiffrer_sad("101", SAD_difficile(A4, N4, E4), N4))
    print(dechiffrer_sad(13, A4, determine_faciliteur(E4, N4), N4))

    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!')
    # ex de con 2
    A5 = [3, 4, 9, 19, 38, 77]
    E5 = 27
    N5 = 155
    print(chiffrer_sad("001110", SAD_difficile(A5, N5, E5), N5))
    print(dechiffrer_sad(232, A5, determine_faciliteur(E5, N5), N5))
    print()
    print(dechiffrer_sad(chiffrer_sad("001110", SAD_difficile(A5, N5, E5), N5), A5, determine_faciliteur(E5, N5), N5))





