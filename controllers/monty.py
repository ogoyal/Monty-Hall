
import random
from views.graph import plot_prob
from helpers.settings import get_trial_number, get_sections


def __init__():
    global mlist, trials, sections

    # S = Sheep ; C = Car
    mlist = ['S','S','C']
    trials = get_trial_number()
    sections = get_sections()


# Choose a door from 3 doors
def choose():
    return random.randrange(0,3,1)


# if user changes choice
def change_choice():
    change_choice = 0
    y = []
    for trial in range(1,trials):
        user = choose()

        if(user == 0):
            if(mlist[1] == 'S'):
                user = 2
            else:
                user = 1
        elif(user == 1):
            if(mlist[0] == 'S'):
                user = 2
            else:
                user = 0
        else:
            if(mlist[0] == 'S'):
                user = 1
            else:
                user = 0

        if(mlist[user] == 'C'):
            change_choice += 1

    y += [change_choice/float(trial)]

    return y


# if user doesn't change choice
def same_choice():
    same_choice = 0
    y = []
    for trial in range(1, trials):
        user = choose()

        if(mlist[user] == 'C'):
            same_choice += 1

    y += [same_choice/float(trial)]
    return y


def display_prob(y1,y2):
    # Get color from helper
    # Get title from helper

    x = range(1,trials, sections)
    plot_prob(x,y1[0::sections],y2[0::sections],trials)

if __name__ == "__main__":

    change_prob = change_choice(trials)
    same_prob = same_choice(trials)

    print("Same Choice: ", same_prob)  		# Converges to 33%
    print("Change Choice: ", change_prob)	# Converges to 66%
