# functions


def statement_generator(text, decoration):
    # make string with 3 characters
    ends = decoration * 3
    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def yes_no(question):
    while True:
        # ask the user if they want to read the instructions.
        answer = input(question).lower()
        if answer == "yes" or answer == "y":
            return "yes"
        elif answer == "no" or answer == "n":
            return "no"
        else:
            print("please choose a valid answer")


# main routine
statement_generator("Roll it 13", "🎲")
want_instructions = yes_no("Would you like to read the instructions? ")
print(f"you chose {want_instructions}")

roll_again = yes_no("Would you like to roll again?")
print(f"you chose {roll_again}")

