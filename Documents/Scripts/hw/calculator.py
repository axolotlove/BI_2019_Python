number1 = int(input())
operator = input()
number2 = int(input())
result = 0
if operator == '+':
    result = number1 + number2
    print(result);
elif operator == '-':
    result = number1 - number2
    print(result);
elif operator == '/':
    result = number1 / number2
    print(result);
elif operator == '*':
    result = number1 * number2
    print(result);
else:
    print('Операция не поддерживается')
