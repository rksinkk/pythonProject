#. Организовать и вывести последовательность и:з N случайных целых чисел. Из исходной последовательности
# организовать последовательность, содержащую положительные числа и последовательность,
# содержащую отрицательные числа. Найти количество элементов
#в полученных последовательностях.
import random
N = 10
sequence = [random.randint(-10, 10) for _ in range(N)]
print("Исходная последовательность:", sequence)
positive_sequence = [x for x in sequence if x > 0]
negative_sequence = [x for x in sequence if x < 0]
count_positive = len(positive_sequence)
count_negative = len(negative_sequence)
print("Положительные числа:", positive_sequence, "Количество:", count_positive)
print("Отрицательные числа:", negative_sequence, "Количество:", count_negative)