def group_equal(els):
    seen = {}
    n = 0
    for i in range(len(els) - 1):
        if els[i] == els[i + 1]:
            if els[i] not in seen:
                seen[els[i]] = [els[i]]
            else:
                seen[els[i]].append(els[i])
        else:
            if els[i] == els[i - 1]:
                seen[els[i]].append(els[i])
            else:
                n += 1
                seen['solo' + str(n)] = [els[i]]
    if els[len(els) - 1] == els[len(els) - 2]:
        seen[els[len(els) - 1]].append(els[len(els) - 1])
    else:
        n += 1
        seen['solo' + str(n)] = [els[len(els) - 1]]
    result = []
    for value in seen.values():
        result.append(value)
    return result


els = [str(i) for i in input().split(',')]
print(group_equal(els))
