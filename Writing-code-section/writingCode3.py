def dictionary_maker(name, lesson, s):
    dictionary.setdefault(name, {}).setdefault(lesson, {})["score"] = s


def adding(txt, tnt, tkt):
    global dictionary
    dictionary = dict()
    dictionary_maker("Mamad", "Math", 20)
    dictionary_maker("Alex", "Chemistry", 18)
    dictionary_maker("Selena", "Geometry", 19)
    keyWords = dictionary.keys()
    values = dictionary.values()
    print(f"\n{txt}{dictionary}\n\n{tnt}{keyWords}\n\n{tkt}{values}\n")


def main():
    adding(
        "This is the whole Dictionary: ",
        "These are the keys of Dictionary: ",
        "These are the values of Dictionary: ",
    )


if __name__ == "__main__":
    main()
