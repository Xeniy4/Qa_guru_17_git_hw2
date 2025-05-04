

"""Найдет только доллар"""
def converter_with_or():
    dol = 100
    eur = 120
    print(f'Выберите валюту: dol или eur')
    current = input()
    if current == 'dol' or 'дол' or 'доллар' or 'dollar' or '$':
        print(f'Сколько долларов вы хотите?')
        sum = int(input())
        dol *= sum
        print(f'С вас {dol} рублей')
    elif current == 'eur' or 'евр' or 'евро' or 'euro' or 'Э':
        print(f'Сколько евро вы хотите?')
        sum = int(input())
        eur *= sum
        print(f'С вас {eur} рублей')
    else:
        print(f'валюты {current} у нас нет')


# print(converter_with_or())


"""Найдет выбранную из 2х вариантов валюту 'dol' или 'eur'"""
def converter():
    dol = 100
    eur = 120
    print(f'Выберите валюту: dol или eur')
    current = input()
    if current == 'dol':
        print(f'Сколько долларов вы хотите?')
        sum = int(input())
        dol *= sum
        print(f'С вас {dol} рублей')
    elif current == 'eur':
        print(f'Сколько евро вы хотите?')
        sum = int(input())
        eur *= sum
        print(f'С вас {eur} рублей')
    else:
        print(f'валюты {current} у нас нет')


# print(converter())


"""Найдет только первые параметры 'dol' или 'eur'"""
def converter_with_and():
    dol = 100
    eur = 120
    print(f'Выберите валюту: dol или eur')
    current = input()
    if current == 'dol' and 'дол' and 'доллар' and 'dollar' and '$':
        print(f'Сколько долларов вы хотите?')
        sum = int(input())
        dol *= sum
        print(f'С вас {dol} рублей')
    elif current == 'eur' and 'евр' and 'евро' and 'euro' and 'Э':
        print(f'Сколько евро вы хотите?')
        sum = int(input())
        eur *= sum
        print(f'С вас {eur} рублей')
    else:
        print(f'валюты {current} у нас нет')


print(converter_with_and())
