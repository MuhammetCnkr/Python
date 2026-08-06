fruits = {
    "apple":130,
    "avocado":50,
    "banana":110,
    "cantaloupe":50,
    "grapefruit":60,
    "sweet cherries":100
}
commands = ["quit","extend","list"]

def main():
    print("If you want to extend database, write 'extend'.\nIf you want to quit, write 'quit'.")

    while True:
        while True:
            fruit = (input("Item: ")).strip().lower()

            if fruit in fruits.keys() or fruit in commands:
                break
            else:
                print("Again!")

        if fruit == commands[0]:
            print("Goodbye")
            break
        elif fruit == commands[1]:
            extend()
        elif fruit == commands[2]:
            show()
        else:
            print(f"Calories: {fruits[fruit]}")


def extend():
    fruit_name = (input("Name: ")).strip().lower()
    fruit_calorie = int(input("Calories of fruit: "))
    fruits[fruit_name] = fruit_calorie
def show():
    for k, j in fruits.items():
        print(k, j, sep=": ")

main()
