import random
from time import sleep
import threading


def countdown():
    # Get timer for game
    global _my_timer
    _my_timer = 30
    for x in range(30):
        _my_timer = _my_timer - 1
        sleep(1)

def start_timer():
    # Timer starts
    countdown_thread = threading.Thread(target = countdown)
    countdown_thread.start()

def user_answer():
    # Get answer
    while True:
        user_input = input('Enter an answer: ')
        if not user_input.isdigit():
            print('Numbers only please try again. ')
        else: 
            return int(user_input)

def get_random_nums():
    # Get random numbers for game
        if ['operation'] == '+':
            num1 = random.randint(1, ['max_number'])
            num2 = random.randint(1, ['max_number'])
        elif ['operation'] == 'x':
            num1 = random.randint(1, ['max_number'])
            num2 = random.randint(1, ['max_number'])
        elif ['operation'] == '-':
            num1 = random.randint(1, ['max_number'])
            num2 = random.randint(1, ['max_number'])
            if num2 > num1:
                num2, num1 = num1, num2
        else:
            num2 = random.randint(1, ['max_number'])
            numx = random.randint(1, ['max_number'])
            num1 = num2 * numx
        
        return num1, num2
    
def get_correct_answer():
     # Get correct answer
        if ['operation'] == '+':
            correct = ['num1'] + ['num2']
        elif ['operation'] == '-':
            correct = ['num1'] - ['num2']
        elif ['operation'] == 'x':
            correct = ['num1'] * ['num2']
        else:
            correct = ['num1'] / ['num2']