def main():

    number = int(input("Number: "))
    if number == 0:
        print("1")
    else:
        print(factorial(number))


def factorial(number):

    tutucu = 1
    for i in range(1, number + 1):
        tutucu *= i
    return tutucu


main()
