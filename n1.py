while True:
    name = input("Ваше имя: ")
    if len(name) >= 2 and name[0].isupper() and name [1:].islower() and name.isalpha():
        break
    else:
        print("Недопустимое имя!")
    
while True:
    surname = input("Фамилия: ")
    if len(surname) >= 2 and surname[0].isupper() and surname [1:].islower() and surname.isalpha():
        break
    else:
        print("Недопустимая фамилия!")
    
while True:
    age = input("Возраст: ")
    if age.isdigit() and int(age) > 0 and int(age) <= 120:
        break
    else:
        print("Недопустимый возраст: ")
    
if int(age) % 10 == 1 and int(age) % 100 != 11:
    word = "год"
elif int(age) % 10 > 1 and int(age) % 10 < 5 and (int(age) % 100 < 11 or int(age) % 100 > 15):
    word = "года"
else:
    word = "лет"

print("\nРеализация через format:")
print("Ваше имя: {}, Фамилия: {}, Возраст: {} {}.\n".format(name, surname, int(age), word))

print("Реализация через f-string:")
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {int(age)} {word}.")