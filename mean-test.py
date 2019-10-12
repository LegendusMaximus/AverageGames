input()
import random
wrong = 0
randomnamel = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
randomname1 = random.choice(randomnamel)
randomname2 = random.choice(randomnamel)
randomname3 = random.choice(randomnamel)
randomname = randomname1+randomname2+randomname3
username = input("Enter your username, if you don't have one press enter.")
if username == "":
	username = randomname
	points = 0
	print("Your username is", username)
	print("Assign what we will call you to ", username, " by entering what you would like to be called here. Do not use anything like passwords as this data will be stored in a text file.")
	name = input()
else:
	filename = username+".txt"
	pointsfile = open("c:\\Python\\MeanUsers"+filename)
	pointsstr = pointsfile.readline()
	name = pointsfile.readline()
	points = float(pointsstr)
	print("Welcome back ", name, "!You are starting with", points, "points!")
inp1 = input("Enter a level from 10-100")
if points >= int(inp1):
	print("Please enter a level higher than", points)
	inp1 = input()
while points < int(inp1):
	print("You have", points, "points")
	r1 = random.randint(0, 10)
	r2 = random.randint(0, 10)
	r3 = random.randint(0, 10)
	r4 = random.randint(0, 10)
	meansum = r1+r2+r3+r4
	mean = meansum/4
	print("Enter the mean of ", r1, ",", r2, ",", r3, "and", r4, ".")
	umean = input()
	try:
		umeanint = float(umean)
	except:
		umeanint = 0
	if umeanint == mean:
		print("Correct")
		points += 2
	else:
		print(name, "This is Wrong!")
		points = points-0.7
		wrong += 1
	if wrong == 5:
		print("Your session is ending as you have got too many wrong answers. Enter the code ", username, " when running this again.")
		break
filename = username+".txt"
output = open("c:\\Python\\MeanUsers"+filename, "w")
output.write(str(points)+"\n"+name)
input()