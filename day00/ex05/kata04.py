t = ( 0, 4, 132.42222, 10000, 12345.67)
"""
day = str(t[0])
if int(t[0]) < 10:
    day = "0" + str(t[0])
    
ex = str(t[1])
if int(t[1]) < 10:
    ex = "0" + str(t[1])
    """
print("day_{:02d}, ex_{:02d}, {:.2f}, {:.2e}, {:.2e}".format(t[0], t[1], t[2], t[3], t[4]))

