from collections import Counter

class CharCountTools (object):
    def __init__ (self):
        self.whitespace_labels = {
            ' ' : '<SPACE>',
            '\n' : '<NEWLINE>',
            '\t' : '<TAB>',
        }
    
    def count_char (self, line):
        """read a string and return a counter of characters in the string"""
        char_count = Counter()
        for char in line:
            char_count[self.whitespace_labels.get(char, char)] += 1

        return char_count