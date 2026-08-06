def main():
    fuel_percentage()

def fuel_percentage():

    while True:
        fraction = input("Fraction: ") #1/4, -1/4, 2.5/4, three/four 4/0 5/4
        first_fraction, second_fraction = fraction.strip().split("/")
        try:
            n1 = float(first_fraction)
            n2 = float(second_fraction)
        except ValueError:
            print("Invalid input (string).")
            break

        if int(first_fraction) != n1 or int(second_fraction) != n2:
            raise Exception("Please write integers.")
        elif n2 == 0:
            print("Y must not be 0.")
        elif n1 < 0 or n2 < 0:
            raise ValueError("Please write positive integers")
        elif (n1 - n2) > 0:
            raise Exception("X must be less than Y")
        else:
            if int((n1/n2) * 100) == 0:
                print("E")
            elif int((n1/n2) * 100) == 100:
                print("F")
            else:
                print(f"{int((n1/n2) * 100)}%")


main()
