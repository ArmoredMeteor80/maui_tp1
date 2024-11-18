ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def find(char: str) -> int:
    """Renvoie le code entier d'un caractère dans l'alphabet"""
    return ALPHABET.index(char)


def reverse(msg: str) -> str:
    """Chiffre un message par son écriture à l'envers"""
    return msg[::-1]


if __name__ == '__main__':
    print(find("A"))
    msg = input("Saisir message : ")
    print(reverse(msg))
