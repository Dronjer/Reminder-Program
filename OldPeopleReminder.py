# This program will remind you about drinking water, excercising Eyes and physical activity
# This program will run for 9 am to 5pm that is total tracking time for 8 hours
# Tracking eye exercise for every 30min  and Physical activity after every 45min
# For drinking water we need to remind the user after every 50min
import time

import pygame
from pygame import mixer
import datetime

def get_date_time():
    import datetime
    return datetime.datetime.now()

# Calculating the number seconds for 30min, 45min and 50min
# 1min = 60sec
e = 30*60
p = 45*60
d = 50*60
print(e,p,d)

# Setting the range for a particular day
# Office hour for each day is 8 hours that is 9am to 5pm
t = 8*60*60
print(t)

# starting the mixer
mixer.init()

# Load the music
mixer.music.load("Eye Excercise.mp3")
mixer.music.load("DrinkWater.mp3")
mixer.music.load("Physical Activity.mp3")


# Program for setting timer for eye exercise
while True:
    time.sleep(2)
    print("Take some time for exercising your eyes")
    # Load the music
    mixer.music.load("Eye Excercise.mp3")
    # Play the music
    mixer.music.play()
    query = input(" ")
    if query == 'done':
        # stop the music
        mixer.music.stop()

    time.sleep(5)
    print("Stay Hydrated")
    # Load the music
    mixer.music.load("DrinkWater.mp3")
    # Play the music
    mixer.music.play()
    query = input(" ")
    if query == 'done':
        # stop the music
        mixer.music.stop()

    time.sleep(10)
    print("Perform some physical activity")
    # Load the music
    mixer.music.load("Physical Activity.mp3")
    # Play the music
    mixer.music.play()
    print("Press 'done' to reset the reminder")
    query = input(" ")
    if query == 'done':
        #stop the music
        mixer.music.stop()

    break
