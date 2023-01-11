'''

'''
errors_dict = {'out': 'Вы вышли из системы',
               'noaccess': 'У вас нет доступа в раздел',
               'unknown': 'Неизвестная ошибка',
               'timeout': 'Система долго не отвечает',
               'robot': 'Ваши действия похожи на робота'}


def get_errors(*errors):
    list_of_errors = []
    for error in errors:
        list_of_errors.append(errors_dict[error])
    return list_of_errors


def draw_carpet(weigh, height):
    left_wall = '░▒'
    right_wall = '▒░'
    roof = left_wall + (weigh-4)*'▒' + right_wall
    level = left_wall + (weigh-4)*'▓' + right_wall

    print(roof)
    for i in range(height-2):
        print(level)
    print(roof)


def main():
    draw_carpet(10, 10)


if __name__ == '__main__':
    main()
