total = 0

while True:
    user_input = input("Введите число (или 'stop/end' для завершения): ")

    if user_input.lower() in ['stop', 'end']:
        break

    try:
        number = float(user_input)
        total += number
    except ValueError:
        print("Это не число. Попробуйте снова.")
        continue

print(f"Сумма введённых чисел: {total}")
