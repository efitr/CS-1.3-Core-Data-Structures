#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    # edge cases
    # the pattern is longer than the actual text
    if len(text) <= len(pattern):
        # If they are the same lenght and equal, it's true
        if text == pattern:
            return True
        return False

    if pattern == '':
        return True

    # MENTAL PLAN:
        # Could I do a iterative and recursive solution
    # There are two problems:
        # Going through every single letter in the string
        # if the letters match 

    # go through every letter in the text
    for index, letter in enumerate(text):
        # when the letter is the same has the first place of the pattern
        # The pattern might be here
        current_pattern_position = 0
        #if the current letter equals pattern at position 0
        if letter == pattern[current_pattern_position]:
            #to not break the logic of the first for in case the pattern is not found
            index_in_pattern = index #we create a new index position for the text
            while text[index_in_pattern] == pattern[current_pattern_position]:
                index_in_pattern += 1
                current_pattern_position += 1

                if current_pattern_position == len(pattern):
                    return True
    
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
        if pattern == '':
        return 0
    #I want the position number of the item
    #if contains(text, pattern) == False:
    #    return None
    for index, letter in enumerate(text):

        current_pattern_position = 0
        #if the current letter equals pattern at position 0
        if letter == pattern[current_pattern_position]:
            #to not break the logic of the first for in case the pattern is not found
            index_in_pattern = index #we create a new index position for the text
            while text[index_in_pattern] == pattern[current_pattern_position]:
                index_in_pattern += 1
                current_pattern_position += 1

                if current_pattern_position == len(pattern):
                    return index

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
