'''
Часть 2. Задание со звездочкой
Давайте доработаем логику нашего приложения.
Теперь, если ответ правильный, приложение говорит:
Ответ верный!
Если ответ неверный, приложение говорит:
Осталось попыток: 2, попробуйте еще раз!
Если ответ опять неверный, говорит:
Осталось попыток: 1, попробуйте еще раз!
Если еще раз вводится неправильный ответ, приложение говорит:
Увы, но нет. Верный ответ: ____.
За каждый ответ начисляются баллы.
Если с первой попытки введен правильный ответ - 3 балла,
если со второй - 2 балла, если с третьей - 1.
После ответа на все вопросы приложение говорит:
Вот и все! Вы ответили на ___ вопросов из ___ верно, вы набрали ___ баллов.
'''

import sys
from homework3_1 import welcome_message, percentage_of_completion

questions = ['My name ____ Vova.', 'I ____ a coder.', 'I live ____ Moscow.']
answers = ['is', 'am', 'in']


def answer(task):
    print(task)

    for attempt in range(3):
        score = 3 - attempt
        user_answer = input('Ваш ответ: ')
        if user_answer == answers[questions.index(task)]:
            print('Ответ верный! Вы получаете {} баллов!\n'.format(score))
            return True, score
        else:
            print('Осталось попыток {}. Попробуйте еще раз.\n'.format(score - 1))

    print('Увы, но нет. Верный ответ: {}\n'.format(answers[questions.index(task)]))
    return False, 0


def answer_recursive(task, num_of_attempt=0):
    print(task)
    score = 3 - num_of_attempt
    user_answer = input('Ваш ответ: ')
    if user_answer == answers[questions.index(task)]:
        print('Ответ верный! Вы получаете {} баллов!\n'.format(score))
        return True, score
    else:
        if score - 1 > 0:
            print('Осталось попыток {}. Попробуйте еще раз!\n'.format(score - 1))
            return answer_recursive(task, num_of_attempt + 1)
        else:
            print('Увы, но нет. Верный ответ: {}\n'.format(answers[questions.index(task)]))
            return False, 0


def results(right_answers=1, all_answers=len(questions), score=1, percentage=100, user_name='Denis'):
    print('Вот и все! \nВы ответили на {} вопросов из {} верно, вы набрали {} баллов.'.format(right_answers,
                                                                                              all_answers, score))


def main():
    welcome_message()
    right_answers = 0
    final_score = 0

    for task in questions:
        # user_answer, mark = answer(task)
        user_answer, mark = answer_recursive(task)
        if user_answer:
            right_answers += 1
            final_score += mark

    results(right_answers=right_answers,
            score=final_score,
            percentage=percentage_of_completion(right_answers, len(questions)))


if __name__ == '__main__':
    main()
