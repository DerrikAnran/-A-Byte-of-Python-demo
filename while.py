#!/usr/bin/python
#Filename:while.py
number = 23
running = True
while running:
    guess = int(raw_input('Enter an integer:'))
    if guess == number:
        print'Congratulations,you guessed it.'
        running = False #this cause the while loop to stop
    elif guess < number:
        print'No,it is a little higher than that.'
    else:
        print'No,it is a little lower than that.'
else:
    print'The whole loop is over.'
print'Done!'
