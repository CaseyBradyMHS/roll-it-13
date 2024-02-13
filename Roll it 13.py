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


# main routine
yes_dictionary = {
    "yes",
    "YES",
    "Yes"
}
no_dictionary = {
    "no",
    "NO",
    "No"
}
error = "please choose a valid answer"
keep_going = ""
while keep_going == "":

    # ask the user if they want to read the instructions.
    want_instructions = input("Would you like to read the instructions? ")
    if want_instructions in yes_dictionary:
        print("answer yes was chosen")
        keep_going = input("press enter to go again or any key to stop. ")
    elif want_instructions in no_dictionary:
        print("answer no was chosen")
        keep_going = input("press enter to go again or any key to stop. ")
    else:
        print(error)
