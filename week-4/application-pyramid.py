def main():
    height = int(input("height: "))
    pyramid(height)

def pyramid(n):
     for i in range(int((n+1)/2)):
        j = 2 * i + 1
        print(" " * int(((n - j) / 2)), end ="")
        print("#" * j)


main()

