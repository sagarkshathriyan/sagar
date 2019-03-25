#to find sum of 3 numbers and return zero if two numbers are equal
n1=int(input("Enter the value of 1st number"))
n2=int(input("Enter the value of 2nd number"))
n3=int(input("Enter the value of 3rd number"))
s=n1+n2+n3
if n1==n2 or n2==n3 or n1==n3:
	print("0")
else:
	print(s)