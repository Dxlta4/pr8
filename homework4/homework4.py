while True:
    try:
        # Ввод чисел a и b с проверкой
        a = float(input("Введите первое число a: "))
        b = float(input("Введите второе число b: "))
        break
    except ValueError:
        print("Ошибка: Введите числа.")

# Находим целые границы
start = int(a)  # включаем целое значение a
end = int(b)    # включаем целое значение b

# Вывод целых чисел между a и b
if start < end:
    for i in range(start + 1, end):  # выводим числа между a и b
        print(i, end=" ")
elif start > end:
    for i in range(start - 1, end, -1):  # выводим числа между b и a в обратном порядке
        print(i, end=" ")
else:
    print("Между указанными числами нет целых чисел.")
