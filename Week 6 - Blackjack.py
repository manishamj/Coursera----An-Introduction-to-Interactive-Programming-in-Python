# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user31_OVIykO4Wjj_0.py

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
busted = False
score_player = 0
score_dealer = 0

total_player = 0
total_dealer = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = [] 	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        pr_str = "Hand contains "
        for card in self.hand:
            pr_str += str(card)
            pr_str += " "
        return pr_str

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        
        total = 0
        ace = 0
        for card in self.hand:
            total += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ace = 10
        if total <= 11:
            total += ace
            return total
        else:
            return total
   
    def draw(self, canvas, pos):
       # draw a hand on the canvas, use the draw method for cards
        
        for card in self.hand:
            card.draw(canvas,[pos[0],pos[1]])
            pos[0] += CARD_SIZE[0] + 5
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []  
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))


    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck) 

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        pr_str = "Deck contains "
        for card in self.deck:
            pr_str += str(card)
            pr_str += " "
        return pr_str


#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, total_player, total_dealer, score_dealer

    # Prepare Deck, Player/Dealer and lets play
    outcome = ""
    busted = False
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    total_player = player_hand.get_value()
    
    print "Players's Hand: " + player_hand.__str__()
    #print "Players's Value: " + str(player_hand.get_value())
    print "Players's Value: ", total_player
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    total_dealer = dealer_hand.get_value()
    #total_dealer = 17
    
    print "Dealer's Hand: " + dealer_hand.__str__()
    #print "Dealer's Value: " + str(dealer_hand.get_value())
    print "Dealer's Value: ", total_dealer
    
    print "player: " + str(score_player)
    print "dealer: " + str(score_dealer)
    
    if in_play == True:
        score_dealer += 1
        
    
    in_play = True

def hit():
    # replace with your code below
    # if the hand is in play, hit the player  
    # if busted, assign a message to outcome, update in_play and score
    
    global total_player, in_play, outcome, score_player, score_dealer, player_hand
    
    if in_play == True:
        
#        if total_player == 21:
#            score_player += 1
#            outcome = "You win Blackjack!"
#            in_play = False
#            return    
#        if total_player <= 21:
        player_hand.add_card(Deck.deal_card(deck))
        total_player = player_hand.get_value()
            
        print "Player's Hand: " + player_hand.__str__()
        print "Player's Value: " + str(player_hand.get_value())
            
        # check if new player value is > 21 or 21
        if total_player > 21:
            score_dealer += 1
            outcome = "You have busted!"
            busted = True
            in_play = False
            return
        elif total_player == 21:
            if total_dealer == total_player:
                score_dealer += 1
                outcome = "It is a Tie! Dealer Wins!"
                in_play = False
                return
            else:
                score_player += 1
                outcome = "You Win Blackjack!"
                in_play = False
                return
        else:
#            outcome = "Dealer wins!"
#            score_dealer += 1
#            in_play = False
            return
#    else:
#        return  
       
def stand():
    # replace with your code below
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    
    global total_player, total_dealer, in_play, outcome, score_player, score_dealer
    
    if busted == True:
        outcome = "You have busted!"
        return
    if in_play == True:
        if total_player == 21:
            if total_dealer == total_player:
                score_dealer += 1
                outcome = "It is a Tie! Dealer Wins with " + str(total_player)+"!"
                in_play = False
                return
            else:
                score_player += 1
                outcome = "You win Blackjack with "+ str(total_player)+ " VS " +str(total_dealer)+"!"
                in_play = False
                return 
            
    if in_play == True:
        while total_dealer < 17:
            dealer_hand.add_card(Deck.deal_card(deck))
            total_dealer = dealer_hand.get_value()
            
            print "Dealer's Hand: " + dealer_hand.__str__()
            print "Dealer's Value: " + str(dealer_hand.get_value())
            print "Dealer's Value: ", total_dealer
            
            if total_dealer == 21:
                score_dealer += 1
                outcome = "Dealer Wins!"
                in_play = False
                return
            elif total_dealer > 21:
                score_player += 1
                outcome = "Dealer Busted!! You win Blackjack!"
                in_play = False
                return            
        if total_dealer == total_player:
            score_dealer += 1
            outcome = "It is a Tie! Dealer Wins!"
            in_play = False
            return
        elif total_dealer > total_player:
            score_dealer += 1
            in_play = False
            outcome = "Dealer Wins!"
            return
        elif total_dealer < total_player:
            score_player += 1
            in_play = False
            outcome = "You win Blackjack!"
            return
    else:
        return

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
#    card = Card("S", "A")
#    card.draw(canvas, [300, 300])
    global player_hand, dealer_hand, in_play, outcome, score_player, score_dealer

    canvas.draw_text('Blackjack Game', (90, 60), 50, 'White')
    
    #print Dealer
    # print score
    canvas.draw_text("Score: " + str(score_player - score_dealer), (120, 125), 45, 'White')
    #print Dealer
    canvas.draw_text('Dealer', (10, 160), 30, 'Blue')
    canvas.draw_text('Dealer', (12, 161), 30, 'White')
    dealer_hand.draw(canvas,[10,185])
    if in_play:
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        card_pos = [10 + CARD_BACK_CENTER[0], 185 + CARD_BACK_CENTER[1]]
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, card_pos, CARD_SIZE)
    # print Player
    # print score
    #canvas.draw_text("Player Score: " + str(score_player), (12, 325), 40, 'White')
    
    canvas.draw_text('Player', (10, 350), 30, 'Blue')
    canvas.draw_text('Player', (12, 351), 30, 'White')
    player_hand.draw(canvas,[10,375])
    
    # outcome
    canvas.draw_text(outcome, (10, 550), 40, 'White')
    
    # Next Action messages
    if in_play == True:
        canvas.draw_text("Hit or Stand??", (10, 575), 20, 'White')
    else :
        canvas.draw_text("One More Deal??", (10, 575), 20, 'White')
        
    
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
