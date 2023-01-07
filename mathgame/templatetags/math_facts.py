import random
from time import sleep
import threading
from django import template
from mathgame.models import Mathgame

register = template.Library()

@register.simple_tag
def countdown():
    # Get timer for game
    global _my_timer
    _my_timer = 30
    for x in range(30):
        _my_timer = _my_timer - 1
        sleep(1)

@register.simple_tag
def start_timer():
    # Timer starts
    countdown_thread = threading.Thread(target = countdown)
    countdown_thread.start()

@register.simple_tag
def user_answer():
    # Get answer
    while True:
        user_input = input('Enter an answer: ')
        if not user_input.isdigit():
            print('Numbers only please try again. ')
        else: 
            return int(user_input)

@register.simple_tag
def random_nums():
    # Get random numbers for game
    numList = []
    if Mathgame.operation == '+':
        a = random.randint(1, [Mathgame.max_number])
        b = random.randint(1, [Mathgame.max_number])
        numList.append(a)
        numList.append(b)
    elif Mathgame.operation == 'x':
        a = random.randint(1, [Mathgame.max_number])
        b = random.randint(1, [Mathgame.max_number])
        numList.append(a)
        numList.append(b)
    elif Mathgame.operation == '-':
        a = random.randint(1, [Mathgame.max_number])
        b = random.randint(1, [Mathgame.max_number])
        if b > a:
            b, a = a, b
            numList.append(a)
            numList.append(b)
    else:
        b = random.randint(1, [Mathgame.max_number])
        c = random.randint(1, [Mathgame.max_number])
        a = b * c
        numList.append(a)
        numList.append(b)
    
    return numList

@register.simple_tag 
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