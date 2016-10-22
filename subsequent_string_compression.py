# There is a very simple compression algorithm that takes subsequent
# characters and just emits how often they were seen.

# Example:
# abababaabbbaaaaa

import sys


def compress(string):
    if not string:
        return string
    compressed_string = ''
    num_of_occurrence = 0
    last_char = string[0]
    for char in string:
        if char == last_char:
            num_of_occurrence += 1
        else:
            compressed_string += last_char + str(num_of_occurrence)
            last_char = char
            num_of_occurrence = 1
    compressed_string += last_char + str(num_of_occurrence)
    return compressed_string


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print compress(sys.argv[1])
    else:
        print 'Nothing to compress'
