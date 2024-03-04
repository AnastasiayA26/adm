from math import factorial as fact


def rule_of_sum(set1, set2):
    return set(set1) | set(set2)


def rule_of_product(set1, set2):
    result = [(element1, element2) for element1 in set1 for element2 in set2]
    print(len(result))
    for i in result:
        print(i)
    return len(result)


# сочетания с повторениями
def combinations_with_repetition(elements, length):
    n = len(elements)
    result = fact(n + length - 1) // (fact(n) * fact(length - 1))
    return result


# размещения без повторений
def permutations_without_repetition(elements, length):
    n = len(elements)
    result = fact(n) // fact(n - length)
    return result


# размещения с повторениями
def permutations_with_repetition(elements, length):
    n = len(elements)
    result = n**length
    return result


# сочетания без повторений
def combinations_without_repetition(elements, length):
    n = len(elements)
    result = fact(n) // (fact(length) * fact(n - length))
    return result


# перестановки без повторений
def arrangements_without_repetition(elements, length):
    return fact(len(elements)) // fact(len(elements) - length)


# перестановки с повторениями
def arrangements_with_repetition(elements, lenght):
    k = fact(len(elements))
    for i in range(len(length)):
        k //= fact(int(length[i]))
    return k


# Пример использования программы множественного выбора
choice = int(input("Выберите комбинаторную схему (1-8):"))

if choice == 1:
    set1 = input("Введите первое множество: ").split(",")
    set2 = input("Введите второе множество: ").split(",")
    result = rule_of_sum(set1, set2)
    print("Результат применения правила суммы:", result)

elif choice == 2:
    set1 = input("Введите первое множество: ").split(",")
    set2 = input("Введите второе множество: ").split(",")
    result = rule_of_product(set1, set2)
    print("Результат применения правила произведения:", result)

elif choice == 3:
    elements = input("Введите множество элементов: ").split(",")
    length = int(input("Введите длину размещений с повторениями: "))
    result = permutations_with_repetition(elements, length)
    print("Результат размещения с повторениями:", result)

elif choice == 4:
    elements = input("Введите множество элементов: ").split(",")
    length = int(input("Введите длину размещений без повторениями: "))
    result = permutations_without_repetition(elements, length)
    print("Результат размещений без повторений:", result)

elif choice == 5:
    elements = input("Введите множество элементов: ").split(",")
    length = int(input("Введите длину сочетаний с повторениями: "))
    result = combinations_with_repetition(elements, length)
    print("Результат сочетаний с повторениями:", result)

elif choice == 6:
    elements = input("Введите множество элементов: ").split(",")
    length = int(input("Введите длину сочетаний без повторений: "))
    result = combinations_without_repetition(elements, length)
    print("Результат сочетаний без повторений:", result)

elif choice == 7:
    elements = input("Введите множество элементов: ").split(",")
    length = input("Введите количество повторяющихся элементов: ").split(",")
    result = arrangements_with_repetition(elements, length)
    print("Результат перестановок с повторениями:", result)

elif choice == 8:
    elements = input("Введите множество элементов: ").split(",")
    length = int(input("Введите длину сочетаний без повторений: "))
    result = arrangements_without_repetition(elements, length)
    print("Результат перестановок без повторений:", result)

else:
    print("Некорректный выбор.")
