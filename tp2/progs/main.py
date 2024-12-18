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
        c = (d * msg) % n
        n = len(a)
        for i in range(n - 1, -1, -1):
            if c >= a[i]:
                c -= a[i]
                msg_dechiffre = "1" + msg_dechiffre
            else:
                msg_dechiffre = "0" + msg_dechiffre
        if c == 0:
            return msg_dechiffre
    return "Il n'y a pas de solution avec algo glouton"


def chiffrer_sad(msg: str, b: list, n: int) -> int:
    """Renvoie le message chiffré d'après la clé publique : SAD difficile b et le module n"""
    msg_chiffre = ""
    for i in range(0, len(msg), len(b)):
        bloc = msg[i:i + len(b)]
        bloc_chiffre = 0
        for k in range(len(bloc)):
            bloc_chiffre += int(bloc[k]) * b[k]
        msg_chiffre += str(bloc_chiffre)
    return int(msg_chiffre)


# partie RSA
def dechiffrer_rsa(c: int, d: int, n: int) -> int:
    """Renvoie le message déchiffré c' avec c le message chiffré, d la clé privée, et n = p*q """
    return (c ** d) % n


def chiffrer_rsa(m: int, e: int, n: int) -> int or ValueError:
    """Chiffre le message m à partir de e et n"""
    if m < n:
        return (m ** e) % n
    return ValueError("Erreur, m est supérieur à n")


def chiffrement_msg_rsa(msg: str, e: int, n: int) -> list:
    """Chiffre un message à la manière de l'exercice 3 du TP"""
    msg_chiffre = ""
    lst_cryptogrammes = []
    for char in msg:
        msg_chiffre += "0" + str(find(char)) if find(char) < 10 else str(find(char))
    for i in range(0, len(msg_chiffre), 3):
        paquet = msg_chiffre[i:i + 3]
        lst_cryptogrammes.append(chiffrer_rsa(int(paquet), e, n))
    return lst_cryptogrammes


def dechiffrement_msg_rsa(lst_cryptogrammes: list, d: int, n: int) -> str:
    """Déchiffre un message à la manière de l'exercice 3 du TP"""
    msg_dechiffre = ""
    msg_dechiffre_lettres = ""
    for cryptogramme in lst_cryptogrammes:
        paquet = str(dechiffrer_rsa(cryptogramme, d, n))
        msg_dechiffre += paquet if len(paquet) == 3 else "0" + paquet if len(paquet) == 2 else "0" + paquet
    for i in range(0, len(msg_dechiffre), 2):
        paquet = msg_dechiffre[i:i + 2]
        msg_dechiffre_lettres += ALPHABET[int(paquet)]
    return msg_dechiffre_lettres


def premier_pq(n: int) -> tuple:
    """Renvoie les deux premiers p et q valides où p*q = n """
    for i in range(2, n // 2):
        if est_premier(i):
            p = n // i
            if est_premier(p):
                return p, i
    return 0, 0


if __name__ == '__main__':
    print("⸻⸻⸻⸻⸻⸻ SAD ⸻⸻⸻⸻⸻⸻")
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
    print(f"Pour le message chiffré 262257139 : {dechiffrer_sad(262257139, A, D, N)}")
    print(f"Pour le message chiffré 232680541 : {dechiffrer_sad(232680541, A, D, N)}")

    print()
    print("⸻⸻⸻⸻⸻⸻ RSA ⸻⸻⸻⸻⸻⸻")
    print("⸻⸻⸻ Ex 1 ⸻⸻⸻")
    c, d, n, e = 17, 7, 391, 151
    print(f"1) nombre obtenu : {dechiffrer_rsa(c, d, n)}")
    p, q = premier_pq(n)
    print(f"2) p = {p} et q = {q}")
    phi = (p - 1) * (q - 1)
    print(f"phi = {phi}")
    print(f"3) D = inverse modulaire de E mod phi soit ici = {inverse_modulaire(e, phi)}")
    print("⸻⸻⸻ Ex 2 ⸻⸻⸻")
    n, e, d = 221, 11, 35
    m = 112
    c = 78
    print(f"1) a) le chiffrement de m = 112 renvoie : {chiffrer_rsa(m, e, n)}")
    print(f"b) le déchiffrement de c = 78 renvoie : {dechiffrer_rsa(c, d, n)}")
    p, q = 53, 71
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"2) a) n vaut {n} et phi vaut {phi}")
    e = 307
    print(f"b) e est acceptable si E < phi : {e < phi} et pgcd(phi, e) = 1 : {gcd(phi, e) == 1} donc ici il l'est")
    print(f"D = inverse modulaire de E mod phi soit ici = {inverse_modulaire(e, phi)}")
    print(f"c) Clé publique : E = {e}, N = {n}")
    print(f"Clé privée : D = {d}")
    print(f"d) Il faut se débarasser des éléments restants afin que nul ne puisse recréer notre clé privée car ce sont ses éléments qui ont permis de la définir")
    print("⸻⸻⸻ Ex 3 ⸻⸻⸻")
    e, n = 257, 1073
    d = 353
    print(chiffrement_msg_rsa("RSA", e, n))
    print(dechiffrement_msg_rsa([859, 452], d, n))
    print(chiffrement_msg_rsa("OUI", e, n))
    print(dechiffrement_msg_rsa([105, 578], d, n))

    print(f"a) le chiffrement de METHODE est : {chiffrement_msg_rsa('METHODE', e, n)}")

    print(f"b) le déchiffrement du cryptogramme donne : {dechiffrement_msg_rsa([263, 115, 613, 10], d, n)}")
    print(f"c) le chiffrement de AVEZVOUSBIENREUSSI est : {chiffrement_msg_rsa('AVEZVOUSBIENREUSSI', e, n)}")
    print(f"d) le déchiffrement du cryptogramme donne : {dechiffrement_msg_rsa([1019, 35, 567, 36, 384, 703, 99, 59], d, n)}")
    print(f"e) le déchiffrement du cryptogramme donne : {dechiffrement_msg_rsa([553, 813], d, n)}")
