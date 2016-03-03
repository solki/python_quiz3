# Prompts the user for a word and outputs the list of
# all subwords of the word of height 1.
#
# Written by *** for COMP9021


def extract_subwords(word):
    subwords = []
    subword = ''
    tmp = ''
    word_space_wiped = word.replace(' ', '')
    if word_space_wiped is '':
        return subwords
    for c in word_space_wiped:

        if c is '(':
            subword = tmp + '('
            tmp = ''
        elif c is ')':
            if subword:
                subword += tmp + ')'
                subwords.append(subword)
                subword = ''
                tmp = ''
        elif c is ',':
            if subword:
                subword += tmp + ', '
                tmp = ''
        else:
            tmp += c

    return subwords

word = input('Enter a word: ')
print('The subwords of "{:}" of height 1 are:\n    {:}'.
                                        format(word, extract_subwords(word)))
