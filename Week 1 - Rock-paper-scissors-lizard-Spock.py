# Rock-paper-scissors-lizard-Spock template

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """Returns number corresponding valid name else returns 5."""
    
    # convert name to number using if/elif/else
    # don't forget to return the result!
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print str(name)+" is not a valid choice"
        return 5

def number_to_name(number):
    """Returns given the number returns corresponding name."""
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print str(number)+" is not a valid choice"
        return "None"
    

def rpsls(player_choice): 
    """Returns result of rock, Spock, paper, lizard, scissors""" 
    
    # print a blank line to separate consecutive games
    print
    
    # print out the message for the player's choice
    print "Player chooses "+ str(player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # Take care of non valid player choice
    if player_number == 5:
        return  
    
    # compute random guess for comp_number using random.randrange()
    
    start = 0
    end = 5
    comp_number = random.randrange(start, end)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    if comp_choice == "None":
        return
    
    # print out the message for computer's choice
    print "Computer chooses "+comp_choice

    # compute difference of comp_number and player_number modulo five
    
    difference_mod = (player_number - comp_number) % 5
        
    # use if/elif/else to determine winner, print winner message
    
    if difference_mod == 0:
        print "Player and computer tie!"
    elif difference_mod <= 2:
        print "Player wins!"
    elif difference_mod <= 4:
        print "Computer wins!"
    else:
        print "Oops!! Something went wrong!!"
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
#rpsls(-1)
#rpsls("test")
