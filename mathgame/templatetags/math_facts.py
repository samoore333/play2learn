from datetime import timedelta
from countdowntimer import CountDownTimer
import time
import random
from time import sleep
import threading
from django import template
from mathgame.models import Mathgame

register = template.Library()
    

@register.simple_tag
def user_answer():
    # Get answer
    while True:
        user_input = input('Enter an answer: ')
        if not user_input.isdigit():
            print('Numbers only please try again. ')
        else: 
            return int(user_input)

@register.simple_tag # Random number generator
def randNum(start, stop):
    return random.randint(start, stop)

@register.simple_tag
def randomNum():
    # Get random numbers for game
    if Mathgame.operation == '+':
        num1 = random.randint(1, [Mathgame.max_number])
        num2 = random.randint(1, [Mathgame.max_number])
    elif Mathgame.operation == '*':
        num1 = random.randint(1, [Mathgame.max_number])
        num2 = random.randint(1, [Mathgame.max_number])
    elif Mathgame.operation == '-':
        num1 = random.randint(1, [Mathgame.max_number])
        num2 = random.randint(1, [Mathgame.max_number])
        if num2 > num1:
            num2, num1 = num1, num2
    else:
        num2 = random.randint(1, [Mathgame.max_number])
        numx = random.randint(1, [Mathgame.max_number])
        num1 = num2 * numx

    return num1, num2

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
