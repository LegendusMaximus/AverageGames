input()
user_answer = ""
points = 0
import random	
while True:
	randomq = random.randint(0,100)
	randomq2 = random.randint(0,100)
	operation = ["+", "/", "*", "-"]
	roperation = random.choice(operation)
	question = "Enter the answer to"+str(randomq)+"+"+str(randomq2)
	answer = randomq+randomq2
	print(question)
	while True:
		try:
			user_answer = int(input())
			break
		except:
			points = points-200
			print("Wrong! This is not a number")
			print("You have", points, "points.")
			print(question)
	if user_answer == answer:
		print("Correct!")
		points += 0.108
	elif user_answer == "q":
		break
	else:
		print("Wrong!")
		points = points-100
	print("You have", points, "points!")
input()