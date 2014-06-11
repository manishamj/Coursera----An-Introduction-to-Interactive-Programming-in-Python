# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user30_wzWc36a04ua2oQK.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# Ball related variables
ball_pos = [0, 0]
ball_vel = [0, 0]

# Paddle realted variables - numbers
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0

# Score variable
score1 = 0
score2 = 0

# Acceleration
acceleration = 4


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    """Initialize ball position / velocity by checking direction"""
    
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    # random velocity of the ball
    
    ball_vel = [random.randrange(120, 240) / 60, 
                random.randrange(60, 180) / 60]
    
    # if direction = RIGHT (true)
    
    if (direction):
        ball_vel = [ball_vel[0], -ball_vel[1]]
    else :
        ball_vel = [-ball_vel[0], -ball_vel[1]]
        
# define event handlers

def new_game():
    """Start a new game by resetting global variables and calling spawn ball"""
    
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    #resets
    score1 = 0
    score2 = 0
    
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    
    paddle1_vel = 0
    paddle2_vel = 0
    
    spawn_ball(RIGHT)

def draw(canvas):
    """Draw handler to draw lines, gutters, ball, paddle"""
    
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
       
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    
    # ball hit left paddle or gutter
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ((ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT))
        and (ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT))):
            # Ball hit left paddle
            ball_vel[0] = - (ball_vel[0] * 1.10)
        else :
            # Ball went in left gutter, so other side won
            score2 = score2 + 1
            spawn_ball(RIGHT)
            
    # ball hit right paddle or gutter
    if ball_pos[0] >= WIDTH - 1 - BALL_RADIUS - PAD_WIDTH:
        if ((ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT))
        and (ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT))):
            # Ball hit right paddle
            ball_vel[0] = - (ball_vel[0] * 1.10)
        else :
            # Ball went in right gutter, so other side won
            score1 = score1 + 1
            spawn_ball(LEFT) 
            
    # ball hit top or bottom
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1 - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
            
    # Now update ball postion with ball_vel
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    if ((paddle1_pos + paddle1_vel) >= HALF_PAD_HEIGHT 
        and (paddle1_pos + paddle1_vel) <= (HEIGHT - HALF_PAD_HEIGHT)):
        paddle1_pos = paddle1_pos + paddle1_vel
        
    if ((paddle2_pos + paddle2_vel) >= HALF_PAD_HEIGHT and
        (paddle2_pos + paddle2_vel) <= (HEIGHT - HALF_PAD_HEIGHT)):
        paddle2_pos = paddle2_pos + paddle2_vel 

    # draw paddles
    # Left paddle
    
    point1 = paddle1_pos - HALF_PAD_HEIGHT
    point2 = paddle1_pos + HALF_PAD_HEIGHT
    
    canvas.draw_polygon([(0, point1), (0, point2), (PAD_WIDTH, point2), 
                         (PAD_WIDTH, point1)], 1, 'White', 'White') 
    
    # Right paddle
    
    point3 = paddle2_pos - HALF_PAD_HEIGHT
    point4 = paddle2_pos + HALF_PAD_HEIGHT
    
    canvas.draw_polygon([(WIDTH - 1, point3), (WIDTH - 1, point4), 
                         (WIDTH - 1 - PAD_WIDTH, point4),
                         (WIDTH - 1 - PAD_WIDTH, point3)], 1, 'White', 'White') 
    
    # draw scores
    
    canvas.draw_text(str(score1), (WIDTH / 2 - 75, 50), 50, 'Red')
    canvas.draw_text(str(score2), (WIDTH / 2 + 50, 50), 50, 'Red')
        
def keydown(key):
    """key gets pressed - accelerate per direction of key"""
    
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acceleration
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acceleration
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acceleration
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acceleration

   
def keyup(key):
    """key is relesed - stop the paddle from moving"""
    
    global paddle1_vel, paddle2_vel
    
    if (key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0
    if (key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0



# create frame

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()
