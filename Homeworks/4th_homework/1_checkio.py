def checkio(first, second):
    first = first[1: -1]
    second = second[1: -1]
    words_list1 = first.split(',')
    words_list2 = second.split(',')
    result = []
    for el in words_list1:
        if el in words_list2:
            result.append(el)
    result.sort()
    string_result = ','.join(map(str, result))
    return string_result


first_word = input()
second_word = input()
print(repr(checkio(first_word, second_word)))
