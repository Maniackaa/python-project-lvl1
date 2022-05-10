#!/usr/bin/env python


def main():
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
    print('What number is missing in the progression?')
    return name


def question():
    from random import randint
    item = randint(1, 100)
    correct_answer = 'no'
    if item % 2 == 0:
        correct_answer = 'yes'
    print(f'Question: {item}')
    return correct_answer


def answer():
    q = 'Answer "yes" if the number is even, otherwise answer "no".'
    return input(q)


def is_answer_correct(question, answer):
    if question == answer:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
