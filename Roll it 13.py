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


def instructions():
    statement_generator("Instructions / information", "=")
    print('''
This program is a recreation of the dice game "Roll it 13."
    ''')
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
            print("please enter either yes or no.")


# main routine
# statement_generator("Roll it 13", "🎲")
keep_going = ""
while keep_going == "":
    want_instructions = yes_no("Would you like to read the instructions? ")
    if want_instructions == "yes":
        print("instructions placeholder")

    print("program continues")
