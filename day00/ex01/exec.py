import sys

argc = len(sys.argv) - 1
i = argc 
while (i >= 1):
    s = sys.argv[i]
    str_len = len(s) # calculate length of the list
    res = s[str_len::-1] # slicing 
    res = res.swapcase()
    print (res, end = ' ')
    i = i - 1