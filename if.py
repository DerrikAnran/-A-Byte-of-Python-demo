#!/usr/bin/python
#Filename:if.py
number = 23
guess = int(raw_input('Enter an integer:'))
if guess == number:
    print 'Congratulations,you guessed it.'#New block starts here
    print"(but you do not win any prizes!)"#New block ends here
elif guess < number:
    print'No,it is a litter higher than that.'#Another block
    #You can do whatever you want in ablock...
else:
    print'No,it is a litter lower than that'
    #you must have guess > num to reach here
print'Done!'
#This last statement is always executed, after the if statement is executed.
