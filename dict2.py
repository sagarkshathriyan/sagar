import random
d={8:37,11:2,13:34,28:4,38:9,40:68,65:46,52:87,89:70,93:64,76:97}

p = random.choice([2,8,11,34,98,89,93,52,40])

print("yougot",p)

if p in d:
	if p>d[p]:
		print("snake")
	else:
		print("ladder")

		print("you can go to",d[p])