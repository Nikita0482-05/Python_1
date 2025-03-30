while True:
    num = input("Введите число: ")

    if num == "exit":
        print("Выход из программы...")
        break

    if num.isdigit():
        k = len(num)
        print(f"В этом числе {k} цифры.\n")
    elif num.lstrip('-').isdigit() and num.count('-') == 1:
        k = len(num) - 1
        print(f"В этом числе {k} цифры.\n")
    else:
        print("Ошибка: данные не являются числом.\n")
