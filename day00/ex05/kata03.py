phrase = "The right format"
pad_len = 42 - len(phrase)
for i in range(0, pad_len - 1):
    print("-", end='')
print(phrase)