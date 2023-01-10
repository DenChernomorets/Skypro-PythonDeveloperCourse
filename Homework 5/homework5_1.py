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

english_words = ['let', 'thought', 'city', 'tree', 'cross',
                 'farm', 'hard', 'might', 'story', 'saw',
                 'far', 'sea', 'draw', 'left', 'late',
                 'run', 'sun', 'while', 'press', 'close',
                 'night', 'real', 'life', 'few', 'north']


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


def main():
    welcome_message()
    answers = []


if __name__ == '__main__':
    main()
