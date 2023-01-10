'''
тут будет описание задачи
через .title()
'''


easy_level_words = {'cat': 'кошка',
                    'dog': 'собака',
                    'house': 'дом',
                    'girl': 'девочка',
                    'mother': 'мать'}

medium_level_words = {'table': 'стол',
                      'doctor': 'доктор',
                      'phone': 'телефон',
                      'finger': 'палец',
                      'work': 'работа'}

hard_level_words = {'microphone': 'микрофон',
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
        return easy_level_words
    elif user_choice == 'средний':
        return medium_level_words
    else:
        return hard_level_words


def answer(words_dict, answers_dict):
    for word in words_dict:
        user_answer = input('{}, {} букв, начинается на {}\n'.format(word, len(words_dict[word]), words_dict[word][0]))
        if user_answer.lower() == words_dict[word]:
            answers_dict[user_answer] = True
            print('Верно. {} это {}.'.format(word, words_dict[word]))
        else:
            answers_dict[user_answer] = False
            print('Неверно. {} это {}.'.format(word, words_dict[word]))
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
