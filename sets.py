def enumerate_list(strings):
    result = []
    count = 0 
    for string in strings:
        if string: 
            result.append(f"{count}. {string}")
            count += 1
    return result
def enumerate_backwards(strings):
    result = []
    count = 0  
    for string in strings:
        if string: 
            reversed_string = string[::-1]
            result.append(f"{count}. {reversed_string}")
            count += 1
    return result
