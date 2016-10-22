
# A multiset or a bag is a collection of elements that can be repeated.
# Contrast with a set, where elements can not be repeated.
# Multisets can be intersected just like sets can be intersected.

# INPUT:
# A = [0, 1, 1, 2, 2, 5]
# B = [0, 1, 2, 2, 2, 6]
# OUTPUT:
# [0, 1, 2, 2]

# INPUT:
# A = [0, 1, 1]
# B = [0, 1, 2, 3, 4, 5, 6]
# OUTPUT:
# [0, 1]

# Write a function to find the intersection of two integer arrays.

import copy
from collections import defaultdict


def calculate_multiset_intersection(a, b):
    intersection = []
    # deepcopy b so it stays intact for other functions
    b = copy.deepcopy(b)
    for number in a:
        if number in b:
            intersection.append(number)
            b.remove(number)
    return intersection


def calculate_multiset_intersection_with_dicts(a, b):
    intersection = []
    compressed_a = defaultdict(int)
    compressed_b = defaultdict(int)

    for number in a:
        compressed_a[number] += 1
    for number in b:
        compressed_b[number] += 1

    for number, num_of_occurrence in compressed_a.iteritems():
        if number in compressed_b:
            if num_of_occurrence < compressed_b[number]:
                intersection.extend([number for i in range(num_of_occurrence)])
            else:
                intersection.extend([number for i in range(compressed_b[number])])
    return intersection

if __name__ == '__main__':
    a = [0, 1, 1, 2, 2, 5]
    b = [0, 1, 2, 2, 2, 6]
    c = calculate_multiset_intersection(a, b)
    d = calculate_multiset_intersection_with_dicts(a, b)
    assert c == [0, 1, 2, 2]
    assert d == [0, 1, 2, 2]

    a = [0, 1, 1]
    b = [0, 1, 2, 3, 4, 5, 6]
    c = calculate_multiset_intersection(a, b)
    d = calculate_multiset_intersection_with_dicts(a, b)
    assert c == [0, 1]
    assert d == [0, 1]

    a = [0, 1, 1]
    b = [3, 4, 5, 6]
    c = calculate_multiset_intersection(a, b)
    d = calculate_multiset_intersection_with_dicts(a, b)
    assert c == []
    assert d == []

    a = []
    b = [3, 4, 5, 6]
    c = calculate_multiset_intersection(a, b)
    d = calculate_multiset_intersection_with_dicts(a, b)
    assert c == []
    assert d == []

    a = [0]
    b = []
    c = calculate_multiset_intersection(a, b)
    d = calculate_multiset_intersection_with_dicts(a, b)
    assert c == []
    assert d == []

    a = [0]
    b = [0]
    c = calculate_multiset_intersection(a, b)
    d = calculate_multiset_intersection_with_dicts(a, b)
    assert c == [0]
    assert d == [0]
