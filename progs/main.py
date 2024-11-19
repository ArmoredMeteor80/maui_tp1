from math import *
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
LEN_ALPHA = len(ALPHABET)


def find(char: str) -> int:
    """Renvoie le code entier d'un caractère dans l'alphabet"""
    return ALPHABET.index(char)


def reverse(msg: str) -> str:
    """Chiffre un message par son écriture à l'envers"""
    return msg[::-1]


def cesar_simple() -> str:
    """Renvoie le message chiffré selon la méthode de César simple"""
    # Chiffrement ou déchiffrement ?
    mode = int(input("Quel mode, chiffrement (1) ou déchiffrement (2) : "))
    b_key = int(input(f"Clé de {"chiffrement" if mode == 1 else "déchiffrement"} : "))
    msg = input(f"Message à {"chiffrer" if mode == 1 else "déchiffrer"} : ")
    msg_y = ""
    for char in msg:
        msg_y += ALPHABET[(find(char) + b_key) % LEN_ALPHA] if mode == 1 else ALPHABET[(find(char) - b_key) % LEN_ALPHA]
    return msg_y


def vigenere() -> str:
    """Renvoie le message chiffré selon la méthode de Vigenère"""
    # Chiffrement ou déchiffrement ?
    mode = int(input("Quel mode, chiffrement (1) ou déchiffrement (2) : "))
    # Cette fois la clé est une chaine de caractères
    b_key = input(f"Clé de {"chiffrement" if mode == 1 else "déchiffrement"} : ")
    msg = input(f"Message à {"chiffrer" if mode == 1 else "déchiffrer"} : ")
    msg_y = ""
    index_b_key = 0
    for char in msg:
        # pour le décalage, on parcourt la clé b via index_b_key qu'on fait modulo la taille de la clé b, on renvoie la position dans l'alphabet par rapport à la lettre
        msg_y += ALPHABET[(find(char) + find(b_key[index_b_key % len(b_key)])) % LEN_ALPHA] if mode == 1 else ALPHABET[(find(char) - find(b_key[index_b_key % len(b_key)])) % LEN_ALPHA]
        index_b_key += 1
    return msg_y


def cesar_affine() -> str:
    """Renvoie le message chiffré selon la méthode de César affine"""
    # Chiffrement ou déchiffrement ?
    mode = int(input("Quel mode, chiffrement (1) ou déchiffrement (2) : "))
    a_key = int(input(f"Clé de {"chiffrement" if mode == 1 else "déchiffrement"} a : "))

    # Tant que le pgcd(a, longueur_alphabet) != 1 on redemande
    while gcd(a_key, LEN_ALPHA) != 1:
        print(f"Le pgcd de la clé a : {a_key} avec la longueur de l'alphabet : {LEN_ALPHA} ne vaut pas 1, saisir une nouvelle clé a : ")
        a_key = int(input(f"Clé de {"chiffrement" if mode == 1 else "déchiffrement"} a : "))

    b_key = int(input(f"Clé de {"chiffrement" if mode == 1 else "déchiffrement"} b : "))
    msg = input(f"Message à {"chiffrer" if mode == 1 else "déchiffrer"} : ")
    msg_y = ""
    for char in msg:
        msg_y += ALPHABET[(a_key*find(char) + b_key) % LEN_ALPHA] if mode == 1 else ALPHABET[inverse_modulaire(a_key)*(find(char) - b_key) % LEN_ALPHA]
    return msg_y


def inverse_modulaire(a: int) -> int:
    """Renvoie l'inverse modulaire de a"""
    r0 = a if a > LEN_ALPHA else LEN_ALPHA
    r1 = LEN_ALPHA if a > LEN_ALPHA else a
    r2 = r0 % r1
    q = r0 // r1
    u0 = 1 if a > LEN_ALPHA else 0
    u1 = 0 if a > LEN_ALPHA else 1
    u2 = u0 - u1*q
    while r2 != 0:
        r0, r1 = r1, r2
        r2 = r0 % r1
        q = r0 // r1
        u0, u1 = u1, u2
        u2 = u0 - u1*q
    return u1+LEN_ALPHA if u1 < 0 else u1


if __name__ == '__main__':
    print("##### Présentation fonction reverse #####")
    msg = "Le monde du fun et du rire !"
    print(f"reverse() prend en paramètre un message, prenons msg = '{msg}'\nreverse() va alors renvoyer : {reverse(msg)}")
    print("\n##### Présentation fonction cesar_simple #####")
    print(f"Le message renvoyé est : {cesar_simple()}")
    print("\n##### Présentation fonction vigenere #####")
    print(f"Le message renvoyé est : {vigenere()}")
    print("\n##### Présentation fonction cesar_affine #####")
    print(f"Le message renvoyé est : {cesar_affine()}")