test_data_pins_evil = [('123', False), ('00011', False), ('1234', False), ('1111', False), ('2222', False),
                       ('3333', False), ('4444', False), ('5555', False), ('6666', False), ('7777', False),
                       ('8888', False), ('9999', False), ('0000', False), ('word', False), ('1let', False),
                       ('111-', False), (')+12', False), ('', False)]

test_data_pins_good = [('1239', True), ('8765', True), ('7801', True), ('0009', True),
                       ('9000', True), ('1703', True), ('6767', True)]

test_data_mails_evil = [('local@skypto', False), ('you(at)sky.pro', False), ('@lizaveta', False), ('mail', False),
                       ('mail', False), ('mail@mail com', False), ('mail@', False)]

test_data_mails_good = [('me@sky.pro', True), ('alarm@gmail.com', True), ('mail.mail@some.com', True)]

test_data_names_evil = [('Р_и_т_а', False), ('К0нстантин', False), ('слово1', False), ('!слово', False),
                       ('Слово?:%!;;%:?*()_!}{:>?', False), ('', False)]

test_data_names_good = [('Данил', True), ('А Ф', True), ('СлОвО ЕщЕ Слово', True), ('К а к о е т о с л о в о ', True),
                       ('Елена', True)]

test_data_passwords_good = [('secretd00r', True), ('huskyeye5', True), ('m3wm3wm3w', True),
                            ('QWE12QW23WE3', True), ('121341231q', True), ('12312314qwqweqwe1e3f4f4f8fjf48hd84dj48f', True),]

test_data_passwords_evil = [('secret', False), ('fh43j_!', False), ('qweasdzxcqweasd', False), ('123', False),
                            ('12341499589000123234', False), ('QWE1', False)]


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
