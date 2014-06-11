# implementation of card game - Memory
# http://www.codeskulptor.org/#user31_YLYq7zSDWCWeEAJ_0.py

import simplegui
import random

cards = range(8) + range(8)
random.shuffle(cards)
exposed = [False] * 16
state = 0
moves = 0
card1 = 0
card2 = 0

WIDTH = 800
HEIGHT = 100
CARD_WIDTH = 50
CARD_HEIGHT = 100
COLUMNS = 16

# helper function to initialize globals
def new_game():
    global cards, moves, state, exposed
    state = 0
    moves = 0
    random.shuffle(cards)
    exposed = [False] * 16

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cards, exposed, state, moves, card1, card2
    
    card_clicked = pos[0] // 50
    
    # Need to see the card is already exposed first
    
    if exposed[card_clicked] == True:
        print "Already opened card clicked!!"
        return
    elif exposed[card_clicked] == False:
        exposed[card_clicked] = True
        if state == 0:
            state = 1
            card1 = card_clicked
            #print state
            #print "card1:", [card1]
        elif state == 1:
            state = 2
            card2 = pos[0]//50
            exposed[card_clicked] = True
            moves += 1
            #print state
            #print "card2:", [card2]

        elif state == 2:
             if cards[card1] != cards[card2]:
                exposed[card1] = False
                exposed[card2] = False
             card1 = pos[0]//50
             #print "card1:", [card1]
             state = 1 
             #print state       
        return card_clicked
    #print state
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    global exposed
    
    number_pos = [0, 80] # evenly space out the cards
    # loop through the deck of cards, start with 
    
    for num in range(len(cards)):
        # if card has not been selected, show blue back
        if not exposed[num]:
            first_point = (num * CARD_WIDTH, 0)
            second_point = ((num * CARD_WIDTH) + CARD_WIDTH, 0)
            third_point = ((num * CARD_WIDTH) + CARD_WIDTH, CARD_HEIGHT)
            fourth_point = (num * CARD_WIDTH, CARD_HEIGHT)
            canvas.draw_polygon([(first_point),
                                 (second_point),
                                 (third_point),
                                 (fourth_point)], 1, "White", "Blue")
        # if card has been selected, show its face    
        else:
            canvas.draw_text(str(cards[num]), number_pos, 85, "White", "sans-serif")
        number_pos[0] += 50    
        
    #update the counter for the number of moves
    label.set_text("Turns = " + str(moves))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
