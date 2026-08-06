import random

def main():
    global random_number, level

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                break

    random_number = random.randint(1, level)

    while True:
        user_number = int(input("Number: "))
        result = distance(user_number)

        match result:
            case "range_error":
                print("Number must not be greater than level")
                continue
            case "not_positive":
                print("Write positive integer")
                continue
            case "right":
                print("Just right!")
                break
            case "large":
                print("Too large!")
            case "small":
                print("Too small!")


def distance(user_number):

    if user_number < 1:
        return "not_positive"
    elif user_number > level:
        return "range_error"
    elif user_number < random_number:
        return "small"
    elif user_number > random_number:
        return "large"
    else:
        return "right"


main()
