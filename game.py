import wikigame

#parsed = wikigame.wikipedia_request("mouse")
#rnd = parsed["query"]["random"][0]["title"]

jumps = 0

seen = set()
current = wikigame.random_article()

with open('./one.txt') as f:
	one = f.read().splitlines()
with open('./two.txt') as f:
	two = f.read().splitlines()
with open('./three.txt') as f:
	three = f.read().splitlines()
with open('./four.txt') as f:
	four = f.read().splitlines()
with open('./five.txt') as f:
	five = f.read().splitlines()
with open('./six.txt') as f:
	six = f.read().splitlines()
with open('./seven.txt') as f:
	seven = f.read().splitlines()

one = [item.lower() for item in one]
two = [item.lower() for item in two]
three = [item.lower() for item in three]
four = [item.lower() for item in four]
five = [item.lower() for item in five]
six = [item.lower() for item in six]
seven = [item.lower() for item in seven]

black = ["Obrestad Lightouse", "Hajar Hajiyeva", "Aeolian Building", "Philippe Close", "Alexander Bruce (architect)", "Chiaramonti Caesar"]
black = [item.lower() for item in black]

#print("Starting at ", current)

flag = False

while (True):
	clinks = [item.lower() for item in wikigame.links_in_order(current)]
	if set(clinks) & set(["frog"]):
		flag = "True"
	if set(clinks) & set(one):
		flag = True
		jumps += 1
		#print("Frog")
	if set(clinks) & set(two):
		flag = True
		jumps += 2
		#print("Mouse")
		#print("Frog")
	if set(clinks) & set(three):
		flag = True
		jumps += 3
		#print("---")
		#print("Rodent")
		#print("Mouse")
		#print("Frog")
	if set(clinks) & set(four):
		flag = True
		jumps += 4
		#print("---")
		#print("Mammal")
		#print("Rodent")
		#print("Mouse")
		#print("Frog")
	if set(clinks) & set(five):
		flag = True
		jumps += 5
		#print("---")
		#print("New Zealand")
		#print("Mammal")
		#print("Rodent")
		#print("Mouse")
		#print("Frog")
	if set(clinks) & set(six):
		flag = True
		jumps += 6
		#print("---")
		#print("Honorific")
		#print("New Zealand")
		#print("Mammal")
		#print("Rodent")
		#print("Mouse")
		#print("Frog")
	if set(clinks) & set(seven) or set(clinks) & set(["turkish language","korean language"]):
		flag = True
		jumps += 7
		#print("---")
		#print("Turkish/korean Language")
		#print("Honorific")
		#print("New Zealand")
		#print("Mammal")
		#print("Rodent")
		#print("Mouse")
		#print("Frog")
	if set(clinks) & set(["politics"]):
		flag = True
		jumps += 8
		#print("---")
		#print("politics")
		#print("Turkish Language")
		#print("Honorific")
		#print("New Zealand")
		#print("Mammal")
		#print("Rodent")
		#print("Mouse")
		#print("Frog")
		
	if flag:
		print(jumps)
		exit()

	seen.add(current)
	links = [item.lower() for item in wikigame.links_in_order(current)]
	links = [link for link in links if not link in seen]
	if len(links) > 0:
		if links[0] not in black:
			current = links[0]
		else:
			current = links[1]
		jumps += 1
		#print(current)
	else:
		#print("!!!")
		current = wikigame.random_article()



