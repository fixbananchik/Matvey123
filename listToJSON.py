def listToJSON(my_list):
    buffer = []
    for element in my_list:
        buffer.append(element.toJSON())
    return buffer