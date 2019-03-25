#to check the number is +,- or 0
num = float(input("Enter a number: "))
def check(num):
	if num > 0:
   		print("Positive number")
	elif num == 0:
  		print("Zero")
	else:
   		print("Negative number")
check(num)
