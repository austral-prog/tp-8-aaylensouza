def index_of_by_index(word, lst, start_index):
    for index, element in enumerate(lst[start_index:], start_index):
        if element == word:
            return index
    return -1
def index_of_empty(lst):
    for index, element in enumerate(lst):
        if element == "":
            return index
    return -1
def index_of(word, lst):
    for index, element in enumerate(lst):
        if element == word:
            return index
    return -1
def put(word, lst):
    for index, element in enumerate(lst):
        if element == "":
            lst[index] = word
            return index
    return -1

def remove(word, lst):
    count = 0
    for index, element in enumerate(lst):
        if element == word:
            lst[index] = ""
            count += 1
    return count
