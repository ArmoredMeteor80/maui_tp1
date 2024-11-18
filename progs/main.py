ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
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
    # Chiffrement
    msg_y = ""
    for char in msg:
        msg_y += ALPHABET[(find(char) + b_key) % LEN_ALPHA] if mode == 1 else ALPHABET[(find(char) - b_key) % LEN_ALPHA]
    return msg_y


if __name__ == '__main__':
    print(cesar_simple())
