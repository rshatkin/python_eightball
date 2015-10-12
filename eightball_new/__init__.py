import random


def main():
    NO_QUESTION = ""
    OUTCOMES = open("outcomes.txt", "r").readlines()


    while True:
        question = raw_input(
            "Ask the magic 8 ball a question: " +
            "(type question and press enter or just enter to quit) ")

        if question == NO_QUESTION:
            break

        print OUTCOMES[random.randint(0, len(OUTCOMES)-1)]


if __name__ == '__main__':
    main()
