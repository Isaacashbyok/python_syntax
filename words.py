def print_upper_words(words):
    '''Print each word on a separate line, in all upper case.
        >>> print_upper_words(['yes', 'no', 'maybe', 'so'])
        YES 
        NO
        MAYBE
        SO
    '''
    
    for word in words:
        print(word.upper())
        
def print_upper_words_e(e_words):
    '''Print each word on a separate line, in all uppercase, if it starts with an E or e.
    
    >>> print_upper_words_e(['Emperor Scorpion', 'Marmoset', 'Emu', 'Blue-tongued Skink', 'Elephant'])
    '''
    
    for word in e_words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())
            

def print_upper_words_general(words, first_letter):
    '''Print each word on a separate line, in all uppercase, if it starts with a given letter
    
    >>> print_upper_words_general(['Emperor Scorpion', 'Marmoset', 'Emu', 'Blue-tongued Skink', 'Elephant'], 
    ... first_letter = ['M', 'B'])
    MARMOSET
    BLUE-TONGUED SKINK
    '''    
    
    for word in words: 
        for letter in first_letter:
            if word.startswith(letter):
                print(word.upper())
                break