
# Write a function that takes maximum 30 characters from a string but without cutting the words.

# Full description:
# Featuring stylish rooms and moorings for recreation boats. Room Mate Aitana is  designer hotel built in 2013 on an
# island in the IJ River in Amsterdam."

# First 30 characters:
# Featuring stylish rooms and mo

# Smarter approach (max 30 characters, no words are broken):
# Featuring stylish rooms and


def smart_substring(string):
    last_word = ''
    smart_substr = ''
    for i in range(len(string)):
        if len(smart_substr) + len(last_word) > 30:
            last_word = ''
            break
        if string[i] != ' ':
            last_word += string[i]
        else:
            smart_substr += last_word
            last_word = ' '
    return smart_substr + last_word


if __name__ == '__main__':
    assert smart_substring('My favourite cake is a chocolate cake with a lot of ganache and some whipped cream.') \
           == 'My favourite cake is a'
    assert smart_substring('') == ''
    assert smart_substring('This is thirty characters long') == 'This is thirty characters long'
