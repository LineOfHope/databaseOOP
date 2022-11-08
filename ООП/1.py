import os

class Auto():
    def __init__(self, marka, god, color, dvigat):
        self.marka = marka
        self.god = god
        self.color = color
        self.dvigat = dvigat

    def __str__(self):
        txt = '1. Марка: ' + self.marka + "\n2. Год: " + str(self.god) + "\n3. Цвет: " + self.color + "\n4. Объем двигателя: " + str(self.dvigat)
        return txt

def SortParam(st):
    return st.marka

autopark = []
chilsa = '1234567890'
sn = []

def proverka(k):
    p = 0
    if len(k) == 0:
        return 0
    else:
        for i in k:
            if i not in chilsa:
                p =1
        if p == 0:
            return 1
        else:
            return 0

if not os.path.exists('save.txt'):
    with open('save.txt', 'w'): pass

with open('save.txt', "r") as f:
    n = f.read().splitlines()

for i in range(len(n)):
    n[i] = n[i].split()
    A = Auto(n[i][0], n[i][1], n[i][2], n[i][3])
    autopark.append(A)

while True:
    os.system('cls')
    print("(1) Создать новый автомобиль\n(2) Просмотр всего каталога автомобилей\n(3) Удалить данные об автомобиле\n(4) Изменить характеристику автомобиля\n(5) Отсортрировать каталог по Марке\n(6) Сохранить и завершить работу\n(7) Завершить работу без сохранения")
    bb = input()

    if bb == '1':
        os.system('cls')
        print("Создание нового автомобиля\n")
        marka = input("Ввдеите марку автомобиля: ")
        while len(marka) == 0:
            marka = input("Вы ничего не ввели: ")
        god = input("Ввдедите год выпуска автомобиля: ")
        while len(god) == 0:
            god = input("Вы ничего не ввели: ")
        while not proverka(god):
            god = input("Введите число: ")
        color = input("Введите цвет автомобиля: ")
        while len(color) == 0:
            color = input("Вы ничего не ввели: ")
        dvigat = input("Введите объем двигателя: ")
        while len(dvigat) == 0:
            dvigat = input("Вы ничего не ввели")
        while not proverka(dvigat):
            dvigat = input("Введите число: ")
        A = Auto(marka, god, color, dvigat)
        autopark.append(A)
        continue

    elif bb == '2':
        os.system('cls')
        if len(autopark) != 0:
            for i in autopark:
                print(i)
                print(' \n-----------------------------------------\n ')
            a = input()
        else:
            input("В каталоге нет данных")

    elif bb == '3':
        os.system('cls')
        if len(autopark) != 0:
            print('Введите номер автомобиля, данные о котором вы хотите удалить (', len(autopark), ')')
            print('(Если вы хотите вернутся введите "отмена")')
            n = input()
            if n != 'отмена':
                while not proverka(n):
                    n = input("Введите число: ")
                while int(n) - len(autopark) > 0:
                    n = input("Ввдеите корректный номер автомобиля: ")
                    while not proverka(n):
                        n = input("Введите число")
                del autopark[int(n)-1]
                input("Удаленно")
        else:
            input("В каталоге нет данных")

    elif bb == '4':
        os.system('cls')
        if len(autopark) != 0:
            print('Введите номер автомобиля, данные о котором вы хотите изменить (', len(autopark), ')')
            print('(Если вы хотите вернутся введите "отмена")')
            n = input()
            if n != 'отмена':
                while not proverka(n):
                    n = input("Введите число")
                while int(n) - len(autopark) > 0:
                    n = input("Ввдеите корректный номер автомобиля: ")
                    while not proverka(n):
                        n = input("Введите число: ")
                print(autopark[int(n) - 1])
                ll = input('\nВведите номер параметра которого хотите изменить: ')
                if ll == '1':
                    os.system('cls')
                    print("Ведите новое название марки")
                    k = input()
                    while len(k) == 0:
                        k = input("Вы ничего не ввели: ")
                    if len(k) != 0:
                        autopark[int(n)-1].marka = k

                elif ll == '2':
                    os.system('cls')
                    print("Ведите новое название года выпуска")
                    k = input()
                    while len(k) == 0:
                        k = input("Вы ничего не ввели: ")
                    if proverka(k):
                        autopark[int(n)-1].god = k
                    else:
                        input("Ошибка в вводе данных")

                elif ll == '3':
                    os.system('cls')
                    print("Ведите новое название цвета")
                    k = input()
                    if len(k) != 0:
                        autopark[int(n)-1].color = k
                    else:
                        input("Ошибвка в вводе данных")

                elif ll == '4':
                    os.system('cls')
                    print("Ведите новое название объема двигателя")
                    k = input()
                    if len(k) != 0 and proverka(k):
                        autopark[int(n)-1].dvigat = k
                    else:
                        input("Ошибвка в вводе данных")
        else:
            input("В каталоге нет данных")

    elif bb == '5':
        os.system('cls')
        if len(autopark) != 0:
            autopark = sorted(autopark, key=SortParam)
            input("Отсортированно")
        else:
            input("В каталоге нет данных")

    elif bb =='6':
        os.system('cls')
        if len(autopark) != 0:
            sohan = []
            for i in range(len(autopark)):
                A = autopark[i].marka + ' ' + autopark[i].god + ' ' + autopark[i].color + ' ' + autopark[i].dvigat
                sohan.append(A)
            with open('save.txt', "w") as f:
                for i in sohan:
                    f.write(i)
                    f.write('\n')
        else:
            open('save.txt', "w")
        input("Сохраненно")
        break
    if bb == '7':
        break
    else:
        input("Пожалуйста введите корректный номер действия")