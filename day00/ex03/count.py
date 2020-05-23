import string

def text_analyzer(text):
    '''Displays the sums of upper chars, lower chars, puctuation chars and spaces in a given text.'''
    if (len(text) == 0):
        print("give me some text...")
        return
    upper_num = 0
    lower_num = 0
    punc_num = 0
    space_num = 0
    for c in text:
        if (c.isupper()):
            upper_num = upper_num + 1
        elif (c.islower()):
            lower_num = lower_num + 1
        elif (c.isspace()):
            space_num = space_num + 1
        elif (c in string.punctuation):
            punc_num = punc_num + 1
    print("The text contains {} characters".format(len(text)))
    print("- {} upper letters".format(upper_num))
    print("- {} lower letters".format(lower_num))
    print("- {} spaces".format(space_num))
    print("- {} punctuation marks".format(punc_num))
    return