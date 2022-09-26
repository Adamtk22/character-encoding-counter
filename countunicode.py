from collections import Counter

from chardet.universaldetector import UniversalDetector

def count_char (line):
    """read a string and return a counter of characters in the string"""
    char_count = Counter()
    for char in line:
        char_count[char] += 1

    return char_count

def detect_encoding (inputfile):
    detector = UniversalDetector()
    for line in open(inputfile, 'rb'):
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    return detector.result['encoding']