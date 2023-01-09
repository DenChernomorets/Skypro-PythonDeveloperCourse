#
'''

'''

def Dollar_to_ruble(money_in_dollars):
    return money_in_dollars * 70.38

def Ruble_to_euro(money_in_rubles):
    return money_in_rubles * 0.0122

def main():
    print(Dollar_to_ruble(Ruble_to_euro(int(input()))))

if __name__ == '__main__':
    main()