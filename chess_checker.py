


#определяем одного ли цвета поля
def Check_color(u1, p1, u2, p2):
    print("по цвету поля ")
    if (u1 + p1) % 2 != (u2 + p2) % 2:
        print("разные")
    else:
        print("одинаковые")

try:

    print("Первое число — номер вертикали (при счете слева направо), второе — номер горизонтали (при счете снизу вверх)")
    a, b = map(int, input("Введите через пробел номер вертикали и горизонтали для первой фигуры: ").split())
    if a > 8 or a < 1 or b > 8 or b < 1:
        
        quit("Ошибка! Нужно ввести число от 1 до 8! Перезапустите программу!")
    numOfFigure = int(
        input("\nВведите номер для определение типа первой фигуры\n1. Ферзь\n2. Ладья\n3. Слон\n4. Конь\n"))
    if numOfFigure > 4 or numOfFigure < 1:
        
        quit("Ошибка! Нужно ввести число от 1 до 4! Перезапустите программу!")
    c, d = map(int, input("Введите через пробел номер вертикали и горизонтали для второй фигуры: ").split())
    if c > 8 or c < 1 or d > 8 or d < 1:
       
        quit("Ошибка! Нужно ввести число от 1 до 8! Перезапустите программу!")

        """Массивы координат фигур для второго хода"""

    A_figs = []
    B_figs = []

   
    #Проверим угрожает ли фезь
    def check_f(a, b, c, d):
        if a == c or b == d or (abs(a - c) == abs(b - d)):
            print("Ферзь угрожает пешке")
        else:
            print("Ферзь не угрожает пешке, ферзь не находится на одной диагонали или вертикали или горизонтали")
            print("Клетки чтобы уничтожить пешку со второго хода")
          
            A_figs.append(a)
            A_figs.append(c)
            B_figs.append(d)
            B_figs.append(b)
            a2 = a3 = a4 = a5 = a
            b2 = b3 = b4 = b5 = b
            while a2 < 8 and b2 < 8:
                a2 += 1
                b2 += 1
                if abs(a2 - c) == abs(b2 - d) or a2 == c or b2 == d:
                    A_figs.append(a2)
                    B_figs.append(b2)
            while a3 < 9 and b3 > 1:
                a3 += 1
                b3 -= 1
                if abs(a3 - c) == abs(b3 - d) or a3 == c or b3 == d:
                    A_figs.append(a3)
                    B_figs.append(b3)
            while a4 > 1 and b4 < 8:
                a4 -= 1
                b4 += 1
                if abs(a4 - c) == abs(b4 - d) or a4 == c or b4 == d:
                    A_figs.append(a4)
                    B_figs.append(b4)
            while a5 > 1 and b5 > 1:
                a5 -= 1
                b5 -= 1
                if abs(a5 - c) == abs(b5 - c) or a5 == c or b5 == d:
                    A_figs.append(a5)
                    B_figs.append(b5)

               
    #аналогично проверяем ладью
    def check_l(a, b, c, d):
        if a == c or b == d:
            print(" ладья находится на одной вертикали или горизонтали - она угрожает пешке")
            
        else:
            print("Ладья не угрожает пешке")
           
            A_figs.append(a)
            A_figs.append(c)
            B_figs.append(d)
            B_figs.append(b)
            print("Клетки чтобы уничтожить пешку со второго хода")

           
#аналогично проверяем слона
    def check_slon(a, b, c, d):
        if abs(a - c) == abs(b - d):
            print("Слон угрожает пешке")
        else:
            print("Слон не угрожает пешке")
            print("Клетки чтобы уничтожить пешку со второго хода")
            a2 = a3 = a4 = a5 = a
            b2 = b3 = b4 = b5 = b
            while a2 < 8 and b2 < 8:
                a2 += 1
                b2 += 1
                if abs(a2 - c) == abs(b2 - d):
                    A_figs.append(a2)
                    B_figs.append(b2)
            while a3 < 9 and b3 > 1:
                a3 += 1
                b3 -= 1
                if abs(a3 - c) == abs(b3 - d):
                    A_figs.append(a3)
                    B_figs.append(b3)
            while a4 > 0 and b4 < 8:
                a4 -= 1
                b4 += 1
                if abs(a4 - c) == abs(b4 - d):
                    A_figs.append(a4)
                    B_figs.append(b4)
            while a5 > 0 and b5 > 1:
                a5 -= 1
                b5 -= 1
                if abs(a5 - c) == abs(b5 - d):
                    A_figs.append(a5)
                    B_figs.append(b5)

    
    #аналогично проверяем коня
    def check_k(a, b, c, d):
        if ((abs(a - c) == 1) and (abs(b - d) == 2)) or ((abs(a - c) == 2) and (abs(b - d) == 1)):
            print("Конь угрожает пешке")
           
        else:
            print("Конь не угрожает пешке")
           
            a2 = a
            b2 = b
            a_potential = [2, 1, 1, 2, -1, -2, -2, -1]
            b_potential = [-1, -2, 2, 1, 2, 1, -1, -2]
            for i in range(8):
                a2 += a_potential[i]
                b2 += b_potential[i]
                if ((abs(a2 - c) == 1) and (abs(b2 - d) == 2)) or ((abs(a2 - c) == 2) and (abs(b2 - d) == 1)):
                    if a2 < 8 and a2 > 1 and b2 < 8 and b2 > 1:
                        A_figs.append(a2)
                        B_figs.append(b2)
                a2 = a
                b2 = b

       
    #Тут тело программы
    Check_color(a, b, c, d)#Проверяем цвет
    #Делаем проверку в засимости от типа фигуры
    if numOfFigure == 1:
        check_f(a, b, c, d)
        for i in range(len(A_figs)):
            print(A_figs[i], B_figs[i])
    if numOfFigure == 2:
        check_l(a, b, c, d)
        for i in range(len(A_figs)):
            print(A_figs[i], B_figs[i])
    if numOfFigure == 3:
        check_slon(a, b, c, d)
        for i in range(len(A_figs)):
            print(A_figs[i], B_figs[i])
    if numOfFigure == 4:
        check_k(a, b, c, d)
        for i in range(len(A_figs)):
            print(A_figs[i], B_figs[i])
except ValueError:
    quit("Ошибка! Перезапустите программу!")
