try:
    def Shiftleft3(A, B, C):
        x = (B, C, A)
    #    list1 = [A, B, C]
    #    list1[0] = B
    #    list1[1] = C
    #    list1[2] = A
        print(x)
except ValueError:
    print("Введите правильное число")
Shiftleft3(A = int(input("A=")), B = int(input("B=")), C = int(input("C=")))