def main():
    global fruits
    fruits = {}
    get_list()
    show_list()


def get_list():
    while True:
        try:
            item = input("Meyve: ")
        except EOFError:
            print()
            break
        else:
            add(item)


def add(item):
    if item in fruits.keys():
        fruits[item] += 1
    else:
        fruits[item] = 1


def show_list():
    #dict_keys = [i for i in fruits.keys()]
    #dict_keys.sort()

    dict_list = list(fruits)
    dict_list.sort()

    for key in dict_list:
        print(f"{fruits[key]} {key.upper()}")


main()
