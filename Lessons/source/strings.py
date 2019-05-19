#!python

import timeit

def contains(text, pattern):
    return iterative_contains(text, pattern)
    # Does not pass the non matching pattern test
    # return recursive_contains(text, pattern)
    # return recursive_contains(text, pattern, 0, 0)

def iterative_contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    if find_index(text, pattern) is None:
        return False
    return True

def recursive_contains(text, pattern, text_index, pattern_index):
    ''' 
    Best case running time: O(pattern_n) under what conditions, if the item is at the start 
    Worst case running time: O(n + n(pattern_n-1)) under what conditions, if the pattern is at the end 
    and there are many almost patters
    '''
# def recursive_contains(text, pattern, text_index = 0, pattern_index = 0):
    if len(text) <= len(pattern):
    # If they are the same lenght and equal, it's true
        if text is pattern:
            return True
        return False

    if pattern is '':
        return True
    

    if pattern_index is len(pattern) - 1:
        return True

    # This is checking for every point in the 
    if text[text_index] is pattern[pattern_index]:
        # if len(pattern)
        return recursive_contains(text, pattern, text_index + 1, pattern_index + 1)

    if text[text_index] is not pattern[pattern_index]:
        if text_index is len(text) - 1 and text[len(text) - 1] is not pattern[0]:
            return False
        return recursive_contains(text, pattern, text_index + 1, 0)


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    ''' 
    Best case running time: O(pattern_n) under what conditions, if the item is at the start 
    Worst case running time: O(n + n(pattern_n-1) + n(pattern_n)) under what conditions, if the pattern is at the end 
    and there are many almost patters? 
    '''

    if len(text) <= len(pattern):
        # If they are the same lenght and equal, it's true
        if text is pattern:
            return 0
        # return None

    if pattern is '':
        return 0
    
    for index in range(len(text)):

        # the len of the text is lower than index + pattern len
        if len(text) < index + len(pattern):
            return None

        if text[index] is pattern[0]:
            for pattern_index, letter in enumerate(pattern):

                if text[index + pattern_index] is not letter:
                    break
                if pattern_index is len(pattern) - 1:
                    return index
            
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    ''' 
    Best case running time: O(pattern_n) under what conditions, if the item is at the start? 
    Worst case running time: O(n + n(pattern_n) + n(pattern_n)) under what conditions, if the pattern is at the end 
    and there are many almost patters? 
    '''
    all_indexes = []

    if len(text) <= len(pattern):
    # If they are the same lenght and equal, it's true
        if text is pattern:
            return [0]
        return all_indexes
        
    if contains(text, pattern) is False:
        return all_indexes

    if pattern is '':
        for index in range(len(text)):
            all_indexes.append(index)
        return all_indexes

    for index in range(len(text)):

        # the len of the text is lower than index + pattern len
        if len(text) < index + len(pattern):
            return all_indexes

        if text[index] is pattern[0]:
            for pattern_index, letter in enumerate(pattern):

                if text[index + pattern_index] is not letter:
                    break
                    
                if pattern_index is len(pattern) - 1:
                    all_indexes.append(index)

    return all_indexes
    


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
