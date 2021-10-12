# remove all the vowels from a given string
def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    new_string = []
    for i in string_:
        if i not in vowels:
            new_string.append(i)
    return "".join(new_string)