from collections import Counter

from chardet.universaldetector import UniversalDetector

def count_char (inputfile, codec):
    """read file and return a list of tuples in (char, count) format"""
    char_count = Counter()
    with open(inputfile, encoding=codec) as file:
        newline = file.readline()
        while newline:
            for char in newline:
                char_count[char] += 1
            newline = file.readline()

    return sorted(char_count.items(), key=lambda x : x[1], reverse=True)

def detect_encoding (inputfile):
    detector = UniversalDetector()
    for line in open(inputfile, 'rb'):
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    return detector.result['encoding']