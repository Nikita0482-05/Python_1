age = input("Введите ваш возраст: ")

if age.isdigit():
    if int(age) >= 18:
        print("Вы совершеннолетний.")
    else:
        print("Вы несовершеннолетний.")
else:
    print("Недопустимое значение!")