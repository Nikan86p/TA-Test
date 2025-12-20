import random as r


def list_maker(tnt):
    for i in range(1, 10):
        num = r.randint(1, 50)
        Num_list.append(num)

    print(f"{tnt}{Num_list}")


def Average(txt):
    a = 0
    lenght = len(Num_list)
    print(f"The lenght of list: {lenght}")
    for i in Num_list:
        # x+=i
        x = a + i
        a = x

    Average = x / lenght
    print(f"{txt}{Average}")


def main():
    global Num_list
    Num_list = []
    list_maker("The List of numbers: ")
    Average("The Average of list is: ")


if __name__ == "__main__":
    main()
