# Write your code here :-)
from microbit import *
import random
# this line is for the random numbers.
Intervals = 1000
number = random.randint(0, 9)
# display.scroll("Press A if you think the number is odd, if not, Press B")
# This is the instruction for users
display.show(number)
# setup everything

while True:
    sleep(Intervals)
    if button_a.is_pressed():
        if number % 2 and Intervals >= 200:
            # This line sets the condition when the number is even.
            # the intervals cannot be minus
            display.show(Image.YES)
            # this is the triger of showing different integers.
            sleep(1000)
            Intervals = Intervals - 50
            # the intervels change the difficulty
        else:
            display.show(Image.NO)
            sleep(1000)
            Intervals = Intervals + 50
        number = random.randint(0, 9)
        display.show(number)
        # These two lines can reset the number
    elif button_b.is_pressed():
        if number % 2:
            display.show(Image.NO)
            sleep(1000)
            Intervals = Intervals + 50
        else:
            display.show(Image.YES)
            sleep(1000)
            Intervals = Intervals - 50
        number = random.randint(0, 9)
        display.show(number)
    else:
        display.show(Image.NO)
        # this means time is out
        sleep(1000)
        Intervals = Intervals + 50
        number = random.randint(0, 9)
        display.show(number)