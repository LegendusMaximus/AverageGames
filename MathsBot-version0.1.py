input()
import random
randomq = random.randint(0,100)
randomq2 = random.randint(0,100)
operation = ["+", "/", "*", "-"]
roperation = random.choice(operation)
question = str(randomq)+roperation+str(randomq2)
print(question)
input()