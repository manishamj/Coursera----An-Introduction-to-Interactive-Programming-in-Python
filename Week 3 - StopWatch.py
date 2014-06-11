# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user30_gmYo9PcTaIQtYsB.py

import simplegui
import math
import time

# define global variables
time = 0
total_stops = 0
correct_stops = 0
timer_started = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    milli = int(t % 10) 
    tmp = t / 10
    minutes = tmp / 60
    sec1 = int((tmp % 60) / 10)
    sec2 = int((tmp % 60) % 10) 
     
    stime = str(minutes) + ":" + str(sec1) + str(sec2) + "." + str(milli)
    
    return stime
    
def format_ratio():
    global total_stops 
    global correct_stops 
    
    ratio = str(correct_stops) + "/"+ str(total_stops)
    return ratio
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_clicked():
    
    global timer_started
    timer.start()
    timer_started = True
 
    
def stop_clicked():
    
