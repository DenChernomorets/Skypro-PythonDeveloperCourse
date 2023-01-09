



def Your_money():
    year = ['Январь', 'Февраль', 'Март', 'Апрель',
        'Май', 'Июнь', 'Июль', 'Август',
        'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    print('Введите накопленные средства.')
    sum = 0
    for mounth in year:
        sum += int(input("{}: ".format(mounth)))
    return sum

def main():
    print('Итого накоплено денег: {} руб.'.format(Your_money()))

if __name__ == '__main__':
    main()
