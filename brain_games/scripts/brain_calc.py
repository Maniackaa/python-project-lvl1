#!/usr/bin/env python
from random import randint


def game():
    name = welcome_user()
    count = 0
    while count < 3:
        q = question()
        a = answer()
        if is_answer_correct(q, a):
            count += 1
            print('Correct')
        else:
            count = 5
    if count == 3:
        print(f'Congratulations, {name}')
    elif count == 5:
        print(f'\'{a}\' это не верный ответ ;( Верный ответ это - \'{q}\'.')
        print(f"Let's try again, {name}")


def welcome_user():
    import prompt
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ', name)
    return name


def question():
    print('What is the result of the expression?')
    a = randint(0, 10)
    sign = randint(1, 3)
    b = randint(0, 10)
    if sign == 1:
        sign_sym = '+'
        correct_answer = a + b
    elif sign == 2:
        sign_sym = '-'
        correct_answer = a - b
    elif sign == 3:
        sign_sym = '*'
        correct_answer = a * b
    print(f'Question: {a} {sign_sym} {b}')
    return correct_answer


def answer():
    answer = input('Your answer(число): ')
    return int(answer)


def is_answer_correct(question, answer):
    return True if question == answer else False


if __name__ == '__main__':
    game()
