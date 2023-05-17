import op


def main():
    n = int(input("Número:"))
    t = op.tamanho(n)
    print(op.invert(n, t - 1))


if __name__ == "__main__":
    main()
