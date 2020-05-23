import sys
import math

def sum(num1, num2):
	return (num1 + num2)
def difference(num1, num2):
	return (num1 - num2)
def product(num1, num2):
	return (num1 * num2)
def quotient(num1, num2):
	if num2 == 0:
		return("ERROR(div by zero)")
	return (num1 / num2)
def remainder(num1, num2):
	if num2 == 0:
		return("ERROR(div by zero)")
	return (num1 % num2)
def inner_print(num1, num2):
	print("Sum:			{}".format(sum(num1, num2)))
	print("Difference:		{}".format(difference(num1, num2)))
	print("Product:		{}".format(product(num1, num2)))
	print("Quotient:		{}".format(quotient(num1, num2)))
	print("Remainder:		{}".format(remainder(num1, num2)))
def error():
	if len(sys.argv) > 3 or len(sys.argv) < 3:
		print("only 2 arguments accepted")
		return -1
	str1 = sys.argv[1]
	str2 = sys.argv[2]
	if (str1.isdigit() and str2.isdigit()):
			return 0
	else:
		print("only integers accepted, not string(s)")
		return -1

if not error():
	inner_print((int)(sys.argv[1]), (int)(sys.argv[2]))
