import sys

if len(sys.argv) != 3:
    print("Error")
if not (isinstance(sys.argv[1], str) and sys.argv[2].isdecimal()):
    print("TypeError")
s = sys.argv[1]
num = int(sys.argv[2])
for char in s:
    if char in ",?.!/;:":
        s = s.replace(char,'')
s_list = s.split(' ')
res_list =[] 
for i in range(len(s_list)):
    if len(s_list[i]) > num:
        res_list.append(s_list[i])
print(res_list)