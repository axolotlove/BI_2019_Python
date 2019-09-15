number1 = input()
operator = input()
number2 = input()
result = 0
if operator == '+':
    print(number1 + number2);
elif operator == '-':
    print(number1 - number2);
elif operator == '/':
    print(number1 / number2);
elif operator == '*':
    print(number1 * number2);
else:
    print('Операция не поддерживается')
