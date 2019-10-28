def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    minimal = min(data)
    maximal = max(data)
    left_edge = minimal
    n = 1
    result = {}
    for current in range(1, (maximal - minimal + 2)):
        if current in data and current - 1 in data and current + 1 not in data:
            result['interval' + str(n)] = (left_edge, current)
            n += 1
            for j in range(current + 1, maximal + 1):
                if j in data and j - 1 not in data and j + 1 in data:
                    left_edge = j
                    break
        elif current in data and current - 1 not in data and current + 1 not in data:
            result['interval' + str(n)] = (current, current)
            n += 1
    result_list = []
    for value in result.values():
        result_list.append(value)
    return result_list


raw_intervals = {int(i) for i in input().split(',')}
print(create_intervals(raw_intervals))
