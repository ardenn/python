def is_isogram(string):
    for value in string:
        if value.isalpha() and string.count(value) > 1:
            return False
    return True

if __name__ == "__main__":
    print(is_isogram("apple"))
    print(is_isogram("foster"))
