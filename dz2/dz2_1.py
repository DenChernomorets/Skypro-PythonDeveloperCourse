'''Техническое задание
1. Сперва программа здоровается и предлагает начать:
Привет! Предлагаю проверить свои знания английского!
        Расскажи, как тебя зовут!

2. Программа считывает имя пользователя и говорит:
Привет, (имя пользователя), начнем тренировку!

3. Программа задает по очереди 3 вопроса:

Задание 1: My name ____ Vova.
Верный ответ: is

Задание 2: I ____ a coder.
Верный ответ: am

Задание 3: I live ____ Moscow.
Верный ответ: in

Если ответ правильный, приложение говорит:
Ответ верный! Вы получаете 10 баллов!
Если нет, говорит:
Неправильно. Правильный ответ: ____

Затем приложение задает следубщий вопрос.

4. После ответа на 3 вопроса приложение говорит:
Вот и все, (имя пользователя)!
    Вы ответили на ___ вопросов из ___ верно.
    Вы заработали ___ баллов.
    Это ___ процентов.'''


tasks = {'My name ____ Vova.': 'is',
         'I ____ a coder.': 'am',
         'I live ____ Moscow': 'in'}


def welcome_message():
    user_name = input('''Привет! Предлагаю проверить свои знания английского!
        Расскажи, как тебя зовут!
        ''')
    return user_name


def start_message(username):
    print('Привет, {}, начнем тренировку!'.format(username))


def answer(task):
    print(task)
    user_answer = input('Ваш ответ: ')
    if user_answer == tasks[task]:
        print('''Ответ верный! Вы получаете 10 баллов!''')
        return True
    else:
        print('Неправильно. Правильный ответ: {}'.format(tasks[task]))
        return False


def results(username, right_answers, score, percentage_of_completion):
    print('''Вот и все, {}!
    Вы ответили на {} вопросов из {} верно.'''.format(username, right_answers, len(tasks)))
    print('''Вы заработали {} баллов.
    Это {}%.'''.format(score, percentage_of_completion))


def main():
    user_name = welcome_message()
    start_message(user_name)
    final_score, right_answers = 0, 0
    for task in tasks:
        if answer(task):
            right_answers += 1
            final_score += 10
    percentage_of_completion = round((right_answers / len(tasks)) * 100, 1)
    results(user_name, right_answers, final_score, percentage_of_completion)


if __name__ == '__main__':
    main()
