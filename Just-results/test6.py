def my_complex_function_1(grades, file_name):
    try:
        with open(file_name, "w") as file:
            for i in grades:
                if i == grades[-1]:
                    file.write(f"{i}")
                else:
                    file.write(f"{i},")
    except:
        print("Too Bad! Exception happened!")


def my_complex_function_2(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            print(text)
    except:
        print("Too Bad! Exception happened! Maybe the file does not exist?!")


def my_complex_function_3(file_name):
    try:
        with open(file_name, "r") as file:
            text_lines = file.read_lines()
            for line in text_lines:
                print(line)
    except:
        print("Too Bad! Exception happened! Maybe the file does not exist?!")


grades = [1, 2, 3, 4, 10, 12, 15, 16, 3]
print(grades[-1])
my_complex_function_1(
    grades,
    "/Users/nikan86p/Downloads/Nikan-mabani/TA-test/Just-results/my_text_file.txt",
)
my_complex_function_2(
    "/Users/nikan86p/Downloads/Nikan-mabani/TA-test/Just-results/my_text_file.txt"
)
my_complex_function_3(
    "/Users/nikan86p/Downloads/Nikan-mabani/TA-test/Just-results/my_text_file.txt"
)
