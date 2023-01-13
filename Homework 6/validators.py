'''
Создайте файл validators.py, в нем создайте функции:
check_pin() - проверяет, является ли строка четырехбуквенным пин-кодом.
Пин-код не может содержать 4 одинаковых цифры и быть равен 1234
check_pass() - проверяет, чтобы пароль был не меньше 9 символов,
содержал буквы и цифры
check_mail() - проверяет наличие собаки и точки
check_name() - проверяет содержание в имени только русских букв и пробелов.
'''
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
    regular_pin = r'\b\d{4}\b'
    if re.match(regular_pin, user_pin):
        return True
    else:
        return False
'''
def check_pass(user_pass):
    '''
    check_pass() - проверяет, чтобы пароль был не меньше 9 символов,
    содержал буквы и цифры
    '''
    pass

def check_mail(user_mail):
    '''
    check_mail() - проверяет наличие собаки и точки
    '''
    pass

def check_name(user_name):
    '''
    check_name() - проверяет содержание в имени только русских букв и пробелов.
    '''
    pass


def check_pin(user_pin):
    try:
        if int(user_pin) > 999 and int(user_pin) < 10000 and str(user_pin) == user_pin:
            if not user_pin[0] == user_pin[1] == user_pin[2] == user_pin[3]:
                if int(user_pin) != 1234:
                    return True
    except:
        return False
    return False


def main():
    while True:
        print(check_pin(input()))


if __name__ == '__main__':
    main()
