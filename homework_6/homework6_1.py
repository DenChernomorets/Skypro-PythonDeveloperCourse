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
# line * height name roof == border line level = middle line
    border_line = '░▒' + (weigh-4)*'▒' + '▒░'
    middle_line = ' ░▒' + (weigh-4)*'▓' + '▒░'

    print(border_line + '\n', (middle_line + '\n')*height, border_line)


def main():
    draw_carpet(10, 15)


if __name__ == '__main__':
    main()
