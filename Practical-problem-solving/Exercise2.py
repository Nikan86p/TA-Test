def score(txt, tnt):
    score_list = [53, 96, 85, 32, 70, 90]
    high_scores = []
    for i in score_list:
        if i >= n:
            # print(i)
            high_scores.append(i)

    High = list(reversed(sorted(high_scores)))
    lenght = len(high_scores)
    highest = High[0]
    print(f"\n{txt}{lenght}")
    print(f"\n{tnt}{highest}\n")


def main():
    global n
    n = 60
    score(f"The lenght of scores equal or higher than {n}: ", "The Highest score: ")


if __name__ == "__main__":
    main()
