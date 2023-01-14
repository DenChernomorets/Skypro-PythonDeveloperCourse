'''
Часть 1. Простая
В этом задании мы дорабатываем приложение из прошлого урока.
Создайте 2 списака с вопросами и ответами.
questions = ['My name ____ Vova.', 'I ____ a coder.', 'I live ____ Moscow.']
answers = ['is', 'am', 'in']
Сперва программа здоровается и предлагает начать:
Привет! Предлагаю проверить свои знания английского!
Набери 'ready', чтобы начать!
Если пользователь набрал 'ready' - программа начинает задавать вопросы.
Если нет - программа завершается с сообщением:
Кажется, вы не хотите играть. Очень жаль.
Когда первый вопрос задан, программа ждет ввод пользователя.
Если ответ правильный, приложение говорит:
Ответ верный!
Если нет, говорит:
Неправильно. Правильный ответ: ____
Затем приложение задает следующий вопрос.
После ответа на все вопросы приложение говорит:
Вот и все! Вы ответили на ___ вопросов из ___ верно. Это ___ процентов.
Кстати, если вы поменяете кол-во вопросов, приложение все равно должно верно считать статистику!
'''


import sys

questions = ['My name ____ Vova.', 'I ____ a coder.', 'I live ____ Moscow.']
answers = ['is', 'am', 'in']


def welcome_message():
    while True:
        if input('''Привет! Предлагаю проверить свои знания английского!
        Набери 'ready', чтобы начать!
        ''') == 'ready':
            break
        else:
            print('Кажется, вы не хотите играть. Очень жаль.')
            sys.exit()


def answer(task):
    print(task)
    user_answer = input('Ваш ответ: ')
    if user_answer == answers[questions.index(task)]:
        print('Ответ верный!\n')
        return True
    else:
        print('Неправильно. Правильный ответ: {}\n'.format(answers[questions.index(task)]))
        return False


def results(right_answers=1, all_answers=len(questions), score=1, percentage=100, user_name='Denis'):
    print('Вот и все! \nВы ответили на {} вопросов из {} верно. Это {}%'.format(right_answers, all_answers, percentage))


def percentage_of_completion(right_answers, all_questions):
    return round((right_answers / all_questions * 100), 1)


def main():
    welcome_message()
    right_answers = 0
    for task in questions:
        if answer(task):
            right_answers += 1
    percentage = percentage_of_completion(right_answers, len(questions))
    results(right_answers=right_answers, percentage=percentage)


if __name__ == '__main__':
    main()
