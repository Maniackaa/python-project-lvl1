#!/usr/bin/env python
from random import randint
from xmlrpc.client import boolean


def main():
    is_chetn = boolean
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while count < 3:
        number = randint(1, 100)
        if number % 2 == 0:  # Проверяем четность
            is_chetn = True
        else:
            is_chetn = False
        answer = input('Question: ')

        if answer == 'yes' and is_chetn or answer == 'no' and not is_chetn:
            # ответ верный
            print('Correct!')
            count += 1
        else:  # ответ не верный
            if answer == 'yes' and not is_chetn:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            elif answer == 'no' and is_chetn:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print("Let's try again, Bill!")
            else:
                print('Не понимаю - ошибся. Попробуй снова')
            count = 5

        if count == 3:
            print('Congratulations, Bill!')


if __name__ == '__main__':
    main()
