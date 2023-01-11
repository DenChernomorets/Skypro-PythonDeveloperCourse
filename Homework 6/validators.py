'''
Создайте файл validators.py, в нем создайте функции:
check_pin() - проверяет, является ли строка четырехбуквенным пин-кодом.
Пин-код не может содержать 4 одинаковых цифры и быть равен 1234
check_pass() - проверяет, чтобы пароль был не меньше 9 символов,
содержал буквы и цифры
check_mail() - проверяет наличие собаки и точки
check_name() - проверяет содержание в имени только русских букв и пробелов.
1111
2222
3333
4444
5555
6666
7777

'''

import re

def check_pin(user_pin):
    try:
        if int(user_pin) > 999 and int(user_pin) < 10000 and str(user_pin) == user_pin:
            if user_pin[0] != user_pin[1]:
                if int(user_pin) != 1234:
                    return True
    except:
        return False
    return False

def check_pin_regular(user_pin):
    regular_pin = r'((\d)(?=.\d\1)|(\d)(?<=\2.\d.)' #(?!1111) \b\d{4}\b
    if re.match(regular_pin, user_pin):
        return True
    else:
        return False

#def check_pass(user_pass):

#def check_mail(user_mail):

#def check_name(user_name):


def main():
    while True:
        print(check_pin_regular(input()))


if __name__ == '__main__':
    main()
