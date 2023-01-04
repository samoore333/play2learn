import random
from time import sleep
import threading
import os
from mathgame import models


def countdown():
    # Get timer for game
    global _my_timer
    _my_timer = 30
    for x in range(30):
        _my_timer = _my_timer - 1
        sleep(1)


def user_answer():
    # Get answer
    while True:
        user_input = input('Enter an answer: ')
        if not user_input.isdigit():
            print('Numbers only please try again. ')
        else: 
            return int(user_input)

def random_nums():
    # Get random numbers for math game
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
        
    return int(num1, num2)

def main():
    # Get operation
    oper_sel = sel_operation()
    # Get maximum number
    max_num = max_number()
    os.system('cls')
    # Game starts
    score = 0
    countdown_thread = threading.Thread(target = countdown)
    countdown_thread.start()
    while _my_timer > 0:
        # Get random numbers for math game
        if oper_sel == '+':
            num1 = random.randint(1, max_num)
            num2 = random.randint(1, max_num)
        elif oper_sel == 'x':
            num1 = random.randint(1, max_num)
            num2 = random.randint(1, max_num)
        elif oper_sel == '-':
            num1 = random.randint(1, max_num)
            num2 = random.randint(1, max_num)
            if num2 > num1:
                num2, num1 = num1, num2
        else:
            num2 = random.randint(1, max_num)
            numx = random.randint(1, max_num)
            num1 = num2 * numx
        print(f'{num1} {oper_sel} {num2} = ?')
        print(f'You have {_my_timer} seconds left.')
        answer = user_answer()
        os.system('cls')
        # Get correct answer
        if oper_sel == '+':
            correct = num1 + num2
        elif oper_sel == '-':
            correct = num1 - num2
        elif oper_sel == 'x':
            correct = num1 * num2
        else:
            correct = num1 / num2
        if answer == correct:
            print(f'{answer} is correct!')
            score += 1
        else:
            print(f'{answer} is not correct. Try again! {num1} {oper_sel} {num2} = ?')
            print(f'You have {_my_timer} seconds left.')
            answer = user_answer()
    # Game ends
    os.system('cls')
    print('Time is up!')
    print("Sorry, you didn't get that answer in on time")
    print('You answered', score, 'problems')
    enter = input("Press Enter to play again or enter 'q' to quit: ")
    if enter == '': #hitting enter == '' empty string
        main()
    else:
        exit()


main()