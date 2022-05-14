# Реализуйте функцию is_continuous_sequence(), которая проверяет, является ли переданная последовательность целых чисел возрастающей непрерывно (не имеющей пропусков чисел). Например, последовательность [4, 5, 6, 7] — непрерывная, а [0, 1, 3] — нет. Последовательность может начинаться с любого числа. Главное условие — отсутствие пропусков чисел. Последовательность из одного числа не может считаться возрастающей.

# is_continuous_sequence([10, 11, 12, 13])  # True
# is_continuous_sequence([-5, -4, -3])  # True
# is_continuous_sequence([10, 11, 12, 14, 15])  # False
# is_continuous_sequence([1, 2, 2, 3])  # False
# is_continuous_sequence([7])  # False
# is_continuous_sequence([])  # False
p = [10, 11, 12, 13, 14, 15, ]


def is_cont(p):
    if len(p) < 2:
        return False
    for i in range(1, len(p)):
        if p[i] - p[i - 1] != 1:
            return False
    return True


is_cont(p)
