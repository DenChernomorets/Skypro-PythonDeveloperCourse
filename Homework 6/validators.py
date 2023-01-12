'''
Создайте файл validators.py, в нем создайте функции:
check_pin() - проверяет, является ли строка четырехбуквенным пин-кодом.
Пин-код не может содержать 4 одинаковых цифры и быть равен 1234
check_pass() - проверяет, чтобы пароль был не меньше 9 символов,
содержал буквы и цифры
check_mail() - проверяет наличие собаки и точки
check_name() - проверяет содержание в имени только русских букв и пробелов.
'''

import re
# not pin[0] == pin[1] == ...
def check_pin(user_pin):
    try:
        if int(user_pin) > 999 and int(user_pin) < 10000 and str(user_pin) == user_pin:
            if user_pin[0] != user_pin[1] or user_pin[0] != user_pin[2] or user_pin[0] != user_pin[3]:
                if int(user_pin) != 1234:
                    return True
    except:
        return False
    return False


#(?!2222)(?!3333)(?!4444)(?!5555)(?!6666)(?!7777)(?!8888)(?!9999)(?!0000)(?!1234)
def check_pin_regular(user_pin):
    regular_pin = r'(?!1{4})(?!2{4})(?!3{4})(?!4{4})(?!5{4})(?!6{4})(?!7{4})(?!8{4})(?!9{4})(?!0{4})(?!1234)\b\d{4}\b'
    if re.match(regular_pin, user_pin):
        return True
    else:
        return False


def check_pass(user_pass):
    flag1 = False
    flag2 = False
    if len(user_pass) > 8:
        for letter in user_pass:
            if ord(letter) > 47 and ord(letter) < 58: # a in b
                flag1 = True
            elif ord(letter) > 64 and ord(letter) < 91 or ord(letter) > 96 and ord(letter) < 123: # a in b
                flag2 = True
    if flag1 and flag2:
        return True
    else:
        return False


def check_pass_regular(user_pass):
    regular_pass = r'\b*\d*\w\b'
    if re.match(regular_pass, user_pass):
        return True
    else:
        return False


#def check_mail(user_mail):

#def check_name(user_name):


def main():
    while True:
        print(check_pass_regular(input()))


if __name__ == '__main__':
    main()
