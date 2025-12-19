scores = [45, 78, 88, 60, 32, 95]


def passed_students(num):
    new = []
    for i in num:
        if i >= 60:
            new.append(i)
    lenght = len(new)
    return lenght


def lowest_score(nm):
    ordered_list = sorted(nm)
    return ordered_list[0]


def main():
    print(
        f"\nThe count of student that passed the exam is : {passed_students(scores)}\nThe lowest score that has been gottten by special-person is : {lowest_score(scores)}\n"
    )


if __name__ == "__main__":
    main()
