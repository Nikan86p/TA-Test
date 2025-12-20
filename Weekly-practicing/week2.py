import os


def delete():
    os.system("cls" if os.name == "nt" else "clear")


name = input("What is your name? ")
while True:

    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("Please write a number for your age!!!")

accupation = input("What is your accupation? ")


info_list = []

info_list.append([name, age, accupation])

information_dict = {}

information_dict.setdefault(name, {})["age"] = age
information_dict.setdefault(name, {})["accupation"] = accupation


delete()
print(f"informatin List : {info_list}\n")

print(f"information Dictionary : {information_dict}\n")
