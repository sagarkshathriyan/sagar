#fuction with no variable
def func1():
	print("Hii")
	print("hello")
func1()	
#function with single variable
def func2(a):
	print("Hi"+"/t"+ a)
func2("abd")	
#function to add
def func3(a,b,c):
	d=a+b+c 
	print(a,b,c,d)
func3(2,3,4)

#default functiom
def func4(university="IITS"):
	print("I am from"+"/t"+ university)
func4("IITA")
func4("IITG")
func4()	

def func5(a,b):
	print("hi I am calling other Function")
	c=a+b
	return(c)
def func6():
	print("hello i am going to call function")
	s=func5(3,5)
	print("addition is",s)
func6()	