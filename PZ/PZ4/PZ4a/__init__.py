#Дано вещественное число А и целое число N (>0). Используя один цикл, вывести все целые
# степени числа А от 1 до N.
import random
N = random.randrange(1,10)
print('N = ', N)
#A = random.randrange(-10,10)
A = float(input("Dtlbnt xbckj"))
A = round(A)
print('A = ', A)
P = 1
for i in range(1, N+1):
    P *= A
    print(A," в степени ", i," равно",P)