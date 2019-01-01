"""This is a modified version of the basic C25K app. This script includes
 options to customize the run intervals and modify the warmup time."""

import time #the time module
import webbrowser #the webbrowser module

#for x in range(3):
#    time.sleep(10)
#    print(time.ctime())
#    webbrowser.open("Add links to play different music for run and walk times")

def run_walk_span(lap,rw):
    """Flips between walk and run times for the specified time interval."""
    if rw == 1:
        print("Start running")
    else:
        print("Start walking")
    time.sleep(lap * 60)

name = raw_input("Hi there! Wat's your name?:")
tottime = raw_input("\n{}, How long would you like to run today? Enter time in minutes:".format(name))
warmup = raw_input("\nThe recommended C25K warmup is 5 minutes. How many warmup minutes would you like?")
span = raw_input("\nOne last thing, the C25K recommended run interval for beginners is 1 minute, how much run interval would you like?")

tottime = int(tottime) #the total time
warmup = int(warmup)   #warmup time
span = int(span)       #the run span
flip = 1               #switch to flip between run and walk times
cooldown = 1           #set this to 5 mins after the program is ready

#How do I add time to current time and display?

finishtime = 0 + tottime

#print("Let's get started {}. You will finish running at {}".format(name, finishtime))

#start warmup
if warmup > 0:
    print("The current time is {}".format(time.ctime()))
    print("Start your warm up {}".format(name))
    time.sleep(warmup * 60)

#start run walk time
print("The current time is {}".format(time.ctime()))
print("Time to test your fitness levels!!")

while (tottime-warmup-cooldown) > 0:
    run_walk_span(span, flip) #pass the interval to the function
    tottime = tottime - span
    if flip == 1:             #alternate between run and walk times
        flip = 0
    else:
        flip = 1

print("The current time is {}".format(time.ctime()))
print("Good job {}! Start your cool down".format(name))
time.sleep(cooldown * 60)

print("Bye! See ya later!")
