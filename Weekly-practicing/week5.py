user_data = dict()

while True:
    ask = input("Do you want add a user?? (T or N) ").upper()

    if ask == "T":
        name = input("What is your name?? ")
        while True:
            try:
                age = int(input("How old are you?? "))
                break
            except ValueError:
                print("Please enter a valid number for age!!")

        user_data[name] = age
        continue

    if ask == "N":
        try:
            with open(
                "/Users/nikan86p/Downloads/Nikan-mabani/TA-test/Weekly-practicing/test.csv",
                "w",
            ) as f:
                f.write("Name\tAge\n")
                for key in user_data.keys():
                    f.write(f"{key}\t{user_data[key]}\n")

        except Exception as e:
            print(e)

        try:
            with open(
                "/Users/nikan86p/Downloads/Nikan-mabani/TA-test/Weekly-practicing/test.csv",
                "r",
            ) as f:
                reading = f.read()
                print(reading)
        except Exception as d:
            print(d)
        break

    else:
        print("Write a true alphabet (Y or N)!!! ")
