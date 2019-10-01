def checkio(data: list) -> list:
    nonunique_list = []
    for item in data:
        if data.count(item) > 1:
            nonunique_list.append(item)
    return nonunique_list
