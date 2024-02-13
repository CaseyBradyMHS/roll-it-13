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
    # ask the user if they want to read the instructions.
    answer = input(question).lower()
    if answer == "yes" or "y":
        print("yes was chosen")
    if answer == "no" or "n":
        print("no was chosen")


# main routine
error = "please choose a valid answer"
keep_going = ""
while keep_going == "":
    yes_no("would you like to read the instructions? ")
    