input()
import random
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
else:
	print("Wrong!")
input()