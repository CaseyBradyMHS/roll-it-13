import random


def roll_die():
    result = random.randint(1, 6)
    return result


# main routine

die_roll = roll_die()
print(die_roll)
