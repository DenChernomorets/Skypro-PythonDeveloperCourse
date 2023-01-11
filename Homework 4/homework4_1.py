'''
Приложение хранит русские и анлийские слова и предалагет нам угадывать.
Чтобы нам было проще, програма выдает подсказки с длиной слова и первой буквой.

Основные объекты.
eazy, medium, hard - словари формата {'слово' : 'перевод'}
words - словарь формата {'слово' : 'перевод'}
levels - ранги пользователя в зависимости от успехов
answers - словарь с записями о верных и неверных ответах
'''


easy = {'cat': 'кошка',
        'dog': 'собака',
        'house': 'дом',
        'girl': 'девочка',
        'mother': 'мать'}

medium = {'table': 'стол',
          'doctor': 'доктор',
          'phone': 'телефон',
          'finger': 'палец',
          'work': 'работа'}

hard = {'microphone': 'микрофон',
        'glass': 'стекло',
        'monitor': 'монитор',
        'problem': 'проблема',
        'folder': 'папка'}

levels = {0: 'Нулевой',
          1: 'Так себе',
          2: 'Можно лучше',
          3: 'Норм',
          4: 'Хорошо',
          5: 'Отлично'}


def get_complexity():
    while True:
        user_choice = input('Выберите уровень сложности.\nДоступные уровни: легкий, средний, сложный\n')
        if user_choice.lower() in ['легкий', 'средний', 'сложный']:
            print('Выбран уровень сложности {}. Мы предложим 5 слов, подберите перевод.'.format(user_choice))
            break
    if user_choice == 'легкий':
        return easy
    elif user_choice == 'средний':
        return medium
    else:
        return hard


def answer(words_dict, answers_dict):
    for word in words_dict:
        user_answer = input('{}, {} букв, начинается на {}\n'.format(word.title(),
                                                                     len(words_dict[word]),
                                                                     words_dict[word][0]))
        if user_answer.lower() == words_dict[word]:
            answers_dict[user_answer] = True
            print('Верно. {} это {}.'.format(word.title(), words_dict[word]))
        else:
            answers_dict[user_answer] = False
            print('Неверно. {} это {}.'.format(word.title(), words_dict[word]))
    return answers_dict


def results(answers_dict):
    right_ans = 0
    print('Правильно отвеченные слова: ')
    for ans in answers_dict:
        if answers_dict[ans]:
            print(ans)
            right_ans += 1
    print('Ваш ранг: {}'.format(levels[right_ans]))


def main():
    user_answers = {}
    words = get_complexity()
    input('Нажмите  Enter')
    user_answers = answer(words, user_answers)
    results(user_answers)


if __name__ == '__main__':
    main()
