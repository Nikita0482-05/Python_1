x = input("Введите число: ")  


if x.isdigit() and int(x) != 0:  
    number = int(x)  
    if number % 2 == 0:  
        print(f"Число {number} является чётным")  
    else:  
        print(f"Число {number} не является чётным")  
else:  
    
    if len(x) > 0 and (x[0] == '-' or x == '0'):  
        print("Число не является целым положительным")  
    else:  
        print("Введено не число")  