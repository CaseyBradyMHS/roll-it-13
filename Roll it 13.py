# functions


def statement_generator(text, decoration):
    # make string with 3 characters
    ends = decoration * 2
    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def instructions():
    statement_generator("Instructions", "**")
    print('''
At the start of each round, the user and the computer each roll two dice.  The initial number of points for each player 
is the total shown by the dice.  Then, taking turns, the user and computer each roll a single die and add the result to 
their points.  The goal is to get 13 points (or slightly less) for a given round.  Once you are happy with your number 
of points, you can ‘pass’.
-	If you go over 13, then you lose the round (and get zero points). 
-	If the computer goes over 13, the round ends and your score is the number of points that you have earned.
-	If the computer gets more points than you (eg: you get 10 and they get 11, then you lose your score stays the same).  
-	If you get more points than the computer (but less than 14 points), you win and add your points to your score.  The 
    computer’s score stays the same. 
-	If the first roll of your dice is a double, then your score is increased by double the number of points, provided you 
    win.  If the computer’s first roll of the dice is a double, then its points are not doubled (this gives the human 
    player a slight advantage).

-	The ultimate winner of the game is the first one to get to 50 points.
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

keep_going = ""
while keep_going == "":
    statement_generator("Roll it 13", "🎲")
    want_instructions = yes_no("Would you like to read the instructions? ")
    if want_instructions == "yes":
        instructions()

    print("program continues")
