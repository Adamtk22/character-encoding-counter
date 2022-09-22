from collections import Counter

def count_char (inputfile):
    """read file and return a list of tuples in (char, count) format"""
    char_count = Counter()
    with open(inputfile, encoding='utf-8') as file:
        newline = file.readline()
        while newline:
            for char in newline:
                char_count[char] += 1
            newline = file.readline()

    return sorted(char_count.items(), key=lambda x : x[1], reverse=True)
    