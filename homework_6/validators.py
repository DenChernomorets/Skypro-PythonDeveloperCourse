import re


def check_pass(user_pass):
    """
    check_pass() - проверяет, чтобы пароль был не меньше 9 символов,
    содержал буквы и цифры
    """
    pass


def check_mail(user_mail):
    """
    check_mail() - проверяет наличие собаки и точки
    """
    user_mail_regular = r'[a-zA-Z]*^[_=-)(!@#$%^&*"\"{}\":\']'
    if re.match(user_mail_regular, user_mail):
        return True
    else:
        return False


def check_name(user_name):
    """
    check_name() - проверяет содержание в имени только русских букв и пробелов.
    """
    user_name_regular = r'^[ а-яА-Я ]*$'
    if re.match(user_name_regular, user_name):
        return True
    else:
        return False


def check_pin(user_pin):
    """
    check_pin() - проверяет, является ли строка четырехбуквенным пин-кодом.
    Пин-код не может содержать 4 одинаковых цифры и быть равен 1234
    """
    pin_regular = r'\b\d{4}\b'
    if re.match(pin_regular, user_pin):
        pass
    else:
        return False
    if not user_pin[0] == user_pin[1] == user_pin[2] == user_pin[3]:
        if int(user_pin) != 1234:
            return True
    return False


def main():
    while True:
        print(check_pin(input()))


if __name__ == '__main__':
    main()
