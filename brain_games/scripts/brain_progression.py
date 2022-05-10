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
    print('What number is missing in the progression?')
    return name


def question():
    lenght_progression = randint(3, 15)
    step_progression = randint(2, 5)
    first_item = randint(1, 10)
    hidden_item = randint(2, lenght_progression)
    item_pos = 2
    item = first_item
    stroke = str(first_item) + ' '

    while item_pos <= lenght_progression:
        item += step_progression
        if item_pos == hidden_item:
            stroke += '.. '
            correct_answer = item
        else:
            stroke += str(item) + ' '
        item_pos += 1
    print(f'Question: {stroke}')
    return correct_answer


def answer():
    answer = input('Your answer(число): ')
    return int(answer)


def is_answer_correct(question, answer):
    return True if question == answer else False


if __name__ == '__main__':
    game()
