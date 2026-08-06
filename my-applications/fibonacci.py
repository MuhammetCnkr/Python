def main():
    level = int(input("Number: "))

    print("1 1 ",end="")
    x1, x2 = 1, 1
    for i in range(level-2):
        n = x1 + x2
        print(f"{n} ",end="")
        x1, x2 = x2, n


main()
