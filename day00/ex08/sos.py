import sys
morse_dict = {'S': '...', 'O': '---'}
for c in sys.argv[1] :
    print("{}".format(morse_dict.get(c)), end=' ')