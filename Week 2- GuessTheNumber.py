# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
http://www.codeskulptor.org/#user29_LYYuW8VFGio2M4Q.py

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
guesses_remain = 0
secret_number = 0


def clear_input():
    """ Function to clear the text input field. """
    input.set_text("")

# helper function to start and restart the game
def new_game():
    """ Main function to start/restart game """
    
    global num_range
    global guesses_remain
    global secret_number
    
    print ""
    print 'New Game - Pick a number : Range is from 0 to', num_range
        
    secret_number = random.randrange(0, num_range)
    #print 'Secret number',secret_number
    
    guesses_remain = int(math.ceil(math.log((num_range - 0)+1,2)))
    print 'You have '+ str(guesses_remain) + ' chances to guess the number!'
    

# define event handlers for control panel
def range100():
    """ button that sets up num_range to 100 and restarts the game """
   
    global num_range
    
    num_range = 100
    new_game()
    
def range1000():
    """ button that sets up num_range to 1000 and restarts the game """
    
    global num_range
    
    num_range = 1000
    new_game()
    
def input_guess(guess):
    """ Takes guess and compares it to secret number """	
    
    global num_range
    global guesses_remain
    global secret_number
    
    if (not guess.isdigit()):
        print "This is not a valid guess: " + guess
        print "Please enter digits"
        
    elif int(guess) < 0 or int(guess) > num_range:
        print "This is not a valid guess: " + guess
        print 'Pick a number : Range is from 0 to', num_range
        
    else:
        guess_num = int(guess)
        guesses_remain -=1
        
        if  secret_number > guess_num:
            msg = "Guess Higher!"
        elif secret_number < guess_num:
            msg = "Guess Lower!"
        else:
            msg = "You Win!" 
           
        print "Guess was "+guess
        print 'Number of remaining guesses is ', guesses_remain
    
        if guesses_remain == 0 and msg != "You Win!":
            msg = "You Lose!"
            print "The Secret number was: "+str(secret_number)
            
        print msg
        
        if msg == "You Win!" or msg == "You Lose!":
            new_game()
  
    clear_input()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200,200)

# register event handlers for control elements
button1 = frame.add_button("Range is 0 - 100", range100,200)
button2 = frame.add_button("Range is 0 - 1000", range1000, 200)
input = frame.add_input("Enter a guess", input_guess,200)

# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
