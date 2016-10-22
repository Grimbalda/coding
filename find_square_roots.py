# a = [3, 1, 4, 5, 19, 6]
# b = [14, 9, 22, 36, 8, 0, 64, 25]
#
# Some elements in the second array are squares.
# Print elements that have a square root existing in the first array.


def find_square_roots(a, b):
    found_elements = []
    for number in b:
        if number ** 0.5 in a:
            found_elements.append(number)
    return found_elements


if __name__ == '__main__':
    a = [3, 1, 4, 5, 19, 6]
    b = [14, 9, 22, 36, 8, 0, 64, 25]

    # a = []
    # b = [14, 9, 22, 36, 8, 0, 64, 25]

    # a = [3, 1, 4, 5, 19, 6]
    # b = []

    # a = []
    # b = []
    print find_square_roots(a, b)
