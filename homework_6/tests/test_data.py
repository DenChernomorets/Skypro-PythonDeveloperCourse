test_data_pins_evil = [('123', False), ('12345', False), ('1234', False), ('1111', False), ('2222', False),
                       ('3333', False), ('4444', False), ('5555', False), ('6666', False), ('7777', False),
                       ('8888', False), ('9999', False), ('0000', False), ('word', False), ('1let', False),
                       ('111-', False), (')+12', False), ('', False)]

test_data_pins_good = [('1100', True), ('3367', True), ('7801', True), ('0009', True),
                       ('9000', True), ('1703', True), ('6767', True)]

test_data_mails_evil = [('qwerty@qwe_ru', False), ('qwerty@qw!ru', False), ('почта@пугл.ком', False), ('mail', False),
                       ('mail', False), ('mail@mail com', False), ('mail@', False)]

test_data_mails_good = [('mail@mail.ru', True), ('mail@.com', True), ('mail@.mail', True)]

test_data_names_evil = [('Денис_Че', False), (' ПробелYq', False), ('слово1', False), ('!слово', False),
                       ('Слово?:%!;;%:?*()_!}{:>?', False), ('', False)]

test_data_names_good = [('Денис Че', True), (' Пробел', True), ('СлОвО ЕщЕ Слово', True), ('К а к о е т о с л о в о ', True),
                       ('Денис Черноморец', True)]

test_data_passwords_good = []

test_data_passwords_evil = []


def get_test_data_pins_evil():
    return test_data_pins_evil


def get_test_data_pins_good():
    return test_data_pins_good


def get_test_data_mails_evil():
    return test_data_mails_evil


def get_test_data_mails_good():
    return test_data_mails_good


def get_test_data_names_evil():
    return test_data_names_evil


def get_test_data_names_good():
    return test_data_names_good


def get_test_data_passwords_good():
    return test_data_passwords_good


def get_test_data_passwords_evil():
    return test_data_passwords_evil
