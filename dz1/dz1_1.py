#
'''

'''

def Fahrenheit_to_Celsius(degree_Fahrenheit):
    return (degree_Fahrenheit - 32) * 5 / 9

def main():
    print(Fahrenheit_to_Celsius(int(input())))

if __name__ == '__main__':
    main()