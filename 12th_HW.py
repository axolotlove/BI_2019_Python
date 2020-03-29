# 1. Составить список из чисел от 1 до 1000, которые имеют в своём составе 7.
list1 = [int(i) for i in range(1, 1001)]
list2 = list(filter(lambda el: '7' in str(el), list1))
print(list2)

# 2. Взять предложение Would it save you a lot of time if I just gave up and went mad now?
# и сделать его же без гласных. up: можно оставить в виде списка слов и не собирать строку.
sentence1 = 'Would it save you a lot of time if I just gave up and went mad now?'
list3 = list(map(str, sentence1))
vowels = ('a', 'e', 'i', 'o', 'u')
list4 = list(filter(lambda el: str(el) not in vowels, list3))
sentence1_out = ''.join(list4)
print(sentence1_out)

# 3. Для предложения The ships hung in the sky in much the same way that bricks don't составить словарь,
# где слову соответствует его длина.
sentence2 = "The ships hung in the sky in much the same way that bricks don't"
list5 = sentence2.split(' ')
word_length = {el: len(el) for el in list5}
print(word_length)

# 4*. Для чисел от 1 до 1000 наибольшая цифра, на которую они делятся (1-9).
biggest_denominators = []
for x in range(1, 1001):
    for i in range(9, 0, -1):
        if x % i == 0:
            biggest_denominators.append(i)
            break
print(biggest_denominators)

# 5*. Список всех чисел от 1 до 1000, не имеющих делителей среди чисел от 2 до 9.
prime_numbers = []
for el in range(1, 1001):
    for i in range(2, 10):
        if el % i == 0:
            break
    else:
        prime_numbers.append(el)
print(prime_numbers)
