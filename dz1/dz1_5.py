'''
Скоро зарплата
Зарплата приходит 10-го и 25-го числа каждого месяца.
Несложно посчитать, сколько дней до зарплаты, если сегодня 5-е или 20-е число.
А если 28-e, то сколько осталось дней?
Давайте напишем алгоритм, который считает дни до зарплаты с учетом того, что в месяце всегда 30 дней.
'''

def Nearest_salary(current_date):

    salary_date = 10

    if current_date <= 10:
        return 10 - current_date, salary_date
    elif current_date <= 25:
        salary_date = 25
        return 25 - current_date, salary_date
    else:
        return 10 + (30 - current_date), salary_date


def main():

    current_date = int(input(""))
    nearest_salary, salary_date = Nearest_salary(current_date)

    if nearest_salary == 0:
        print('Ближ. зарплата сегодня!')
    else:
        print('Ближ. зарплата {} числа, через {} д.'.format(salary_date, nearest_salary))


if __name__ == '__main__':
    main()