
def Weather(current_weather):
    if current_weather == "Солнечная":
        print("Возьмите с собой очки.")
    else:
        print("Возьмите с собой зонт.")
    print("Хорошего дня!")

def main():
    Weather(input("Какая сегодня погода?"))

if __name__ == '__main__':
    main()