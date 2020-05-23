import sys

argc = len(sys.argv) - 1 
if (argc != 1) or not(sys.argv[1].isdigit()):
    print("ERROR")
else:
    mod = int(sys.argv[1]) % 2
    if (int(sys.argv[1]) == 0):
        print("I'm Zero.")
    elif (mod > 0):
        print("I'm Odd.")
    else:
        print("I'm Even.")