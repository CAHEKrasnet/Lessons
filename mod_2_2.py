print('Input 3 numbers below>>')
first = input('Input first number> ')
if first.isdigit()==True:
    second = input('Input second number> ')
    if second.isdigit()==True:
        third = input('Input third number> ')
        if third.isdigit() == True:
            if first == second and second == third:
                print(3)
            elif first == second or third == second or first == third:
                print(2)
            elif not (first == second or first == third or second == third):
                print(0)
        else:
            print('Вы ввели не целое число! Пока!')
            exit(0)
    else:
        print('Вы ввели не целое число! Пока!')
        exit(0)
else:
    print('Вы ввели не целое число! Пока!')
    exit(0)
