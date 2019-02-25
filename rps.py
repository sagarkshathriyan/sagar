import random
l=["r","p","s"]
#users choice
u=input("Enter your Choice in(r,p,s)")
print("you choosed",u)
c=random.choice(l)
print("Computer choosed",c)

if u==c:
	print("Its a Tie")
elif u=="r" and c=="p":
	print("computer won")
else:	
	print("You Won")

