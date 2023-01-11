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

def check_pin(user_pin):
    try:
        if int(user_pin) > 999 & int(user_pin) < 10000:
            if user_pin[0] != user_pin[1]:
                if int(user_pin) != 1234:
                    return True
    except:
        return False
    return False

def check_pass(user_pass):

def check_mail(user_mail):

def check_name(user_name):


def main():


if __name__ == '__main__':
    main()
