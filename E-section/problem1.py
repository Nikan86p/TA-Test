number_list = [1, 2, 3, -3, -6, -8, -9]


def count_positive(num):
    new_list = []
    for i in num:
        if i > 0:
            new_list.append(i)
    lenght = len(new_list)
    return lenght


print(
    f"\nThis is the lenght of numbers that they are bigger than zero : {count_positive(number_list)}\n"
)
