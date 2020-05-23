t = (3,30,2019,9,25)

hour = str(t[0])
if int(t[0]) < 10:
   hour = "0" + str(t[0])
print("{}/{}/{} {}:{}".format(t[2], t[3], t[4], hour,t[1]))