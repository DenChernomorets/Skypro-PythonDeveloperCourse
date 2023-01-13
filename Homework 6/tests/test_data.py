test_data_pins_evil = {'123': False,
                       '12345': False,
                       '1234': False,
                       '1111': False,
                       '2222': False,
                       '3333': False,
                       '4444': False,
                       '5555': False,
                       '6666': False,
                       '7777': False,
                       '8888': False,
                       '9999': False,
                       '0000': False,
                       'word': False,
                       '1let': False,
                       '111-': False,
                       '--=+': False,
                       '': False}

test_data_pins_good = {'1100': True,
                       '3367': True,
                       '7801': True,
                       '0009': True,
                       '9000': True,
                       '1703': True,
                       '6767': True}


def get_test_data_pins_evil():
    return test_data_pins_evil


def get_test_data_pins_good():
    return test_data_pins_good