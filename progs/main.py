ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def find(char: str) -> int:
    return ALPHABET.index(char)


if __name__ == '__main__':
    print(find("A"))
