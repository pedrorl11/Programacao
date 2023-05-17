def palin(x):
    y = x.replace(" ", "")
    x = x.replace(" ", "")
    if x == y[::-1]:
        return True
    else:
        return False


def main():
    n = input("")
    if palin(n):
        print("É PALÍNDROMO")
    else:
        print("NÃO É PALÍNDROMO")


if __name__ == "__main__":
    main()