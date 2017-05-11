"""This game lets user guess the roll of a pair of dice.  If the user's guess is greater than the total value of the dice roll, they win!"""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input('Guess a number: '))
  return user_guess
  
def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print ("The maximum possible value is: " + str(max_val) )
    sleep(1)
    user_guess = get_user_guess()

    if (user_guess > max_val):
      	 print ("Invalid number: it is higher than maximum possile value")

    else:
        print ("Rolling...")
        sleep(2)
        print ("First roll is: %d" % (first_roll) )
        sleep(1)
        print ("Second roll is: %d" % (second_roll) )
        sleep(1)
        total_roll = first_roll + second_roll
        print ("Total of both rolls is: %d" % (total_roll) )
        print ("Result...")
        sleep(1)

        if user_guess > total_roll:
           	print ("Congrats!! You won!!")

        else:
            print ("Sorry.. You lost")
            return
    
roll_dice (6)  