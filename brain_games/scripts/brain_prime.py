#!/usr/bin/env python


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
    print('Hello, ', name)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return name


def question():
    from random import randint
    item = randint(3, 100)
    i = 2
    correct_answer = 'yes'
    while i <= item / 2:
        if item % i == 0:
            correct_answer = 'no'
        i += 1
    print(f'Question: {item}')
    return correct_answer


def answer():
    return input('Your answer: ')


def is_answer_correct(question, answer):
    if question == answer:
        return True
    else:
        return False


if __name__ == '__main__':
    game()
