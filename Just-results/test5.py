my_dictionary = dict()
for i in range(1, 3):
    name = input("please enter your name: ")
    age = int(input("please enter your age: "))
    my_dictionary[name] = age

with open(
    "/Users/nikan86p/Downloads/Nikan-mabani/TA-test/Just-results/final_file.csv", "w"
) as f:
    f.write("NAME,AGE\n")
    for key in my_dictionary.keys():
        f.write(f"{key},{my_dictionary[key]}\n")

with open ("/Users/nikan86p/Downloads/Nikan-mabani/TA-test/Just-results/final_file.csv","r") as f:
    x=f.read()
    print(x)


