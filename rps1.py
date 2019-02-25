import random
l=["r","p","s"]
while True:
#users choice
	u=input("Enter your Choice withinin (r,p,s) & if you want to quit press q")
	if u=="q":
		print("Game Over,Better Luck Next Time")
		exit()
	c=random.choice(l)
	print("Computer choosed",c)
#comparing
	if u==c:
		print("Its a Tie")
	elif u=="r" and c=="p":
		print("computer won")
	else:	
		print("you won")

