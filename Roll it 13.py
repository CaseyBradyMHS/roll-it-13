# functions
import random
# dice function


def roll_die():
    die_result = random.randint(1, 6)
    return die_result


def double_roll(who):
    double_score_chance = ""

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score_chance = "You have a chance at double points. "

    # Find the total points (so far)
    first_points = roll_1 + roll_2

    # Show the user the result
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score_chance


# statement generator for titles and subtitles
def statement_generator(text, decoration):
    # make string with 3 characters
    ends = decoration * 2
    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# instructions
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


# checks for integer that is 13 or more
def num_check(question, low):
    valid = False
    while not valid:

        error = f"please enter an integer that is at least 13"

        try:
            # ask for a number
            response = int(input(question))

            # check number is more than 0
            if response > low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


# checks for a yes/no answer to question
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


def get_stats(stats_list):
    stats_list.sort()

    lowest_point = stats_list[0]
    highest_point = stats_list[-1]
    point_average = sum(stats_list) / len(stats_list)
    return [lowest_point, highest_point, point_average]


# main routine
statement_generator("Roll it 13", "🎲")
want_instructions = yes_no("Would you like to read the instructions? ")
if want_instructions == "yes":
    instructions()

target_score = num_check("What score?", 12)
user_score = 0
computer_score = 0
num_rounds = 0
user_points_list = []
computer_points_list = []

while user_score < target_score and computer_score < target_score:
    user_pass = "no"
    computer_pass = "no"
    print("press <enter> to begin this round")
    input()

    user_first = double_roll("Player")
    user_points = user_first[0]
    double_score = user_first[1]

    print(f"you got {user_points} points.")
    print(double_score)

    computer_first = double_roll("Computer")
    computer_points = computer_first[0]

    print(f"the computer got {computer_points} points")

    while computer_points < 13 and user_points < 13:

        num_rounds += 1
        print(f"Round {num_rounds}")

        # If user has 13 points, we can assume they don't want to roll again!
        if user_points == 13:
            user_pass = "yes"

        if user_pass == "no":
            roll_again = yes_no("Do you want to roll the dice (type 'no' to pass): ")
        else:
            roll_again = "no"

        if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move

            # If user goes over 13 points, tell them that they lose and set points to 0
            if user_points > 13:
                print(f"You rolled a {user_move} so your total is {user_points}.  "
                      f"Which is over 13 points. ")

                # reset user points to zero so that when we update their
                # score at the end of round it is correct.
                user_points = 0

                break

            else:
                print(f"You rolled a {user_move} and have a total score of {user_points}.")

        else:
            # If user passes, we don't want to let them roll again!
            user_pass = "yes"

        # if computer has 10 points or more (and is winning), it should pass!
        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = "yes"
        elif user_pass == "yes" and computer_points > user_points:
            computer_pass = "yes"
        # Don't let the computer roll again if the pass condition
        # has been met in a previous iteration through the loop.
        elif computer_pass == "yes":
            pass
        else:
            print("\nPress <enter> to continue...")
            input()

            computer_move = roll_die()
            computer_points += computer_move
            if computer_points > 13:
                print(f"The computer rolled a {computer_move}, taking their points"
                      f" to {computer_points}.  This is over 13 points so the computer loses!")
                computer_points = 0
                break

            else:
                print(f"The computer rolled a {computer_move}.  The computer"
                      f" now has {computer_points}.")
            print()
        if user_points > computer_points:
            result = "You are ahead. "
        elif computer_points > user_points:
            result = "The computer is ahead. "
        else:
            result = "It is currently a tie. "

        print(f"{result} \tUser: {user_points} \t | \t Computer: {computer_points}")

        if computer_pass == "yes" and user_pass == "yes":
            break

    if user_points < computer_points:
        print("You lost this round and no points "
              "have been added to your total score.  The computer's score has "
              f"increased by {computer_points} points.")

        add_points = computer_points

    # currently does not include double points!
    elif user_points > computer_points:
        # Double user points if they are eligible
        if double_score == "You have a chance at double points. ":
            user_points *= 2

        print(f"You won the round and {user_points} points have "
              f"been added to your score ")

        add_points = user_points

    else:
        print(f"The result for this round is a tie.  You and the computer "
              f"both have {user_points} points.")

        add_points = user_points

    # end of a single round

    # If the computer wins, add its points to its score
    if user_points < computer_points:
        computer_score += add_points

    # if the user wins, add their points to their score
    elif user_points > computer_points:
        user_score += add_points
        # if it's a tie, add the points to BOTH SCORES
    else:
        computer_score += add_points
        user_score += add_points

    user_points_list.append(user_points)
    computer_points_list.append(computer_points)

    print()
    print(f"🎲🎲🎲 User: {user_score} points | Computer: {computer_score} points 🎲🎲🎲 ")
    print()

user_stats = get_stats(user_points_list)
comp_stats = get_stats(computer_points_list)

print("Game Stats")
print(f"User     - low {user_stats[0]}\t "
      f"high {user_stats[1]}\t "
      f"average {user_stats[2]}")

print(f"Computer - low {comp_stats[0]}\t "
      f"high {comp_stats[1]}\t "
      f"average {comp_stats[2]}")
