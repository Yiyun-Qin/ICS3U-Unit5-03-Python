#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in May 2022
# This is the math program, showing the actual mark


def mark(level_input):
    # This function returns the mark according to the level
    if level_input == "4+":
        mark = 97
    elif level_input == "4":
        mark = 90
    elif level_input == "4-":
        mark = 83
    elif level_input == "3+":
        mark = 78
    elif level_input == "3":
        mark = 74
    elif level_input == "3-":
        mark = 71
    elif level_input == "2+":
        mark = 68
    elif level_input == "2":
        mark = 64
    elif level_input == "2-":
        mark = 61
    elif level_input == "1+":
        mark = 58
    elif level_input == "1":
        mark = 54
    elif level_input == "1-":
        mark = 51
    elif level_input == "R":
        mark = 25
    else:
        mark = -1
    return mark


def main():
    # This function does check and call function

    # input
    level_string = input(
        "Enter the level you want to convert to a percentage(4+, 4, etc.): "
    )

    # process & output
    print("")
    actual_mark = mark(level_string)
    if actual_mark == 25:
        print("The level R means the mark is below 50%.")
    elif actual_mark > 0:
        print(
            "Level {0} has a middle percentage of {1}%.".format(
                level_string, actual_mark
            )
        )
    else:
        print("Sorry, this is not a valid level.")
    print("\nDone.")


if __name__ == "__main__":
    main()
