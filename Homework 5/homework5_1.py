'''
Мы будем создавать программу, которая, на этот раз,
помогает изучать коды азбуки Морзе.
Для этого наша программа будет конвертировать строки в морзе-код,
а затем проверять ответы пользователя.
Все это с помощью функций.
Составьте список английских слов и фраз, которые будете расшифровывать.
Напишите функцию morse_encode(sentence), которая переводит фразы на
английском языке в последовательность точек и тире.
Напишите функцию get_word(), которая полочует случайное слово из списка.
Создайте в начале программы список answers = []
Напишите функцию print_statistics(), которая на основе
списка answers типа [True, True, False, True] выводит статистику типа
    Всего задачек: 5
    Отвечено верно: 3
    Отвечено неверно: 2
При старте программы вывидите приветсвенную информацию.
'''
import random

morse_codes = {"0": "-----",
               "1": ".----",
               "2": "..---",
               "3": "...--",
               "4": "....-",
               "5": ".....",
               "6": "-....",
               "7": "--...",
               "8": "---..",
               "9": "----.",
               "a": ".-",
               "b": "-...",
               "c": "-.-.",
               "d": "-..",
               "e": ".",
               "f": "..-.",
               "g": "--.",
               "h": "....",
               "i": "..",
               "j": ".---",
               "k": "-.-",
               "l": ".-..",
               "m": "--",
               "n": "-.",
               "o": "---",
               "p": ".--.",
               "q": "--.-",
               "r": ".-.",
               "s": "...",
               "t": "-",
               "u": "..-",
               "v": "...-",
               "w": ".--",
               "x": "-..-",
               "y": "-.--",
               "z": "--..",
               ".": ".-.-.-",
               ",": "--..--",
               "?": "..--..",
               "!": "-.-.--",
               "-": "-....-",
               "/": "-..-.",
               "@": ".--.-.",
               "(": "-.--.",
               ")": "-.--.-"}

english_words = ['let', 'thought', 'city', 'lemon tree', 'cross',
                 'farm', 'hard tasks', 'might', 'story of Alisher', 'saw',
                 'far', 'sea', 'draw', 'left', 'late',
                 'run', 'sun', 'while', 'press', 'close',
                 'night', 'real', 'life', 'few', 'north']


def morse_encode(word, morse_letters=None):
    if morse_letters is None:
        morse_letters = morse_codes
    encoded_word = ''
    for letter in word:
        encoded_word += morse_letters[letter]
    return encoded_word


def get_word(wordlist=None):
    if wordlist is None:
        wordlist = english_words
    random_index = random.randint(0, len(wordlist))
    return wordlist[random_index]


def welcome_message():
    print('Сегодня мы потренируемся расшифровывать морзянку.')
    input('Нажмите Enter, чтобы начать.')


def answer(english_word, user_answers, num_of_question):
    encoded_word = morse_encode(english_word)
    ans = input('Слово {} - {}'.format(num_of_question, encoded_word))
    if ans == english_word():
        print('Верно, {}!'.format(english_word.title()))
        return user_answers.append(True)
    else:
        print('Неверно, {}'.format(english_word).title())
        return user_answers.append(False)


def print_statistics(user_answers):
    correct_ans, incorrect_ans = 0, 0
    for ans in user_answers:
        if ans:
            correct_ans += 1
        else:
            incorrect_ans += 1
    print('''
    Всего задачек: {}
    Отвечено верно: {}
    Отвечено неверно: {}
    '''.format(len(user_answers), correct_ans, incorrect_ans))


def main():
    welcome_message()
    answers = []
    for question in range(5):
        answer(get_word(), answers, question)
    print_statistics(answers)


if __name__ == '__main__':
    main()
