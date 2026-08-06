import random

def main():
    global level_list
    level_list = [1,2,3]

    get_level()

    i = 0
    score = 10
    while i < 10:
        x1, x2 = generate_integer(level), generate_integer(level)

        wrong = 0
        while True:
            if wrong < 3:
                try:
                    user_answer = int(input(f"{x1} + {x2} = "))
                except ValueError:
                    print("EEE")
                else:
                    if (x1+x2) != user_answer:
                        print("EEE")
                        wrong += 1
                    else:
                        break
            else:
                print(f"{x1} + {x2} = {x1+x2}")
                score -= 1
                break


        i += 1


    print(score)



def get_level():
    global level

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in level_list:
                break


def generate_integer(level):

    if level == 1:
        return random.randint(0,10)
    else:
        return random.randint((10 ** (level-1)), 10**level)



if __name__ == "__main__":
    main()
