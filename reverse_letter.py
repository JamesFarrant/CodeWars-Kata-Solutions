def reverse_letter(string):
    return string[::-1] if string.isalpha() else ''.join([i for i in string[::-1] if i.isalpha()])
