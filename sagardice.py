import random
ps=0
di=0

while True:
	r=input("press r to roll the dice")

	if r=="r":
		di=random.randint(1,6)
		print("you have got :",di)

	if di==1 or di==6:
		ps=d
		break

print("congrats you have landed on the board.you are at:",ps)			