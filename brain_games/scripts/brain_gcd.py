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
            print('Correct!')
        else:
            count = 5
    if count == 3:
        print(f'Congratulations, {name}!')
    elif count == 5:
        print(f'\'{a}\' это не верный ответ ;( Верный ответ это - \'{q}\'.')
        print(f"Let's try again, {name}")


def welcome_user():
    import prompt
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    return name


def question():
    a = randint(0, 100)
    b = randint(0, 100)
    count = 1
    n = 1
    while count <= min(a, b):
        if a % count == 0 and b % count == 0:
            n = count
        count += 1
    print(f'Question: {a} {b}')
    return n


def answer():
    answer = input('Your answer(число): ')
    return int(answer)


def is_answer_correct(question, answer):
    return True if question == answer else False


if __name__ == '__main__':
    game()
