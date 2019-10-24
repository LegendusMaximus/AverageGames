input()
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
	user_answer = int(input())
	if user_answer == answer:
		print("Correct!")
		points += 0.108
	else:
		print("Wrong!")
		points = points-100
	print("You have", points, "points!")
input()