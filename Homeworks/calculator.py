print("Введите первое число, оператор (+ - / *) и второе число")
number1 = float(input())
operator = input()
number2 = float(input())
result = 0
if operator == '+':
    result = number1 + number2
    print(result)
elif operator == '-':
    result = number1 - number2
    print(result)
elif operator == '/' & number2 != 0:
    result = number1 / number2
    print(result)
elif operator == '/' & number2 == 0:
    print("Невозможно деление на 0")
elif operator == '*':
    result = number1 * number2
    print(result)
else:
    print('Операция не поддерживается')
