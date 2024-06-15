# Для каждого столбца матрицы с четным номером найти сумму ее элементов.
# В матрице найти минимальный элемент в
# предпоследнем столбце.
import random
matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(row)

sums = []
for col in range(len(matrix[0])):
    if col % 2 != 0:
        column_sum = sum(matrix[row][col] for row in range(len(matrix)))
        sums.append(column_sum)
print("Суммы элементов для столбцов с четным номером:", sums)

min_element = min(row[-2] for row in matrix)
print("Минимальный элемент в предпоследнем столбце:", min_element)