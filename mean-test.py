input()
wrong5 = 0
import random
username = input("Enter your username, if you don't have one press enter.")

play = True
while play == True:	
	randomnamel = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
	randomname1 = random.choice(randomnamel)
	randomname2 = random.choice(randomnamel)
	randomname3 = random.choice(randomnamel)
	randomname = randomname1+randomname2+randomname3
	if username == "":
		username = randomname
		points = 0
		wrong = 0
		correct = 0
		print("Your username is", username)
		print("Assign what we will call you to ", username, " by entering what you would like to be called here. Do not use anything like passwords as this data will be stored in a text file.")
		name = input()
	else:
		filename = username+".txt"
		pointsfile = open("c:\\Python\\MeanUsers\\"+filename)
		pointsstr = pointsfile.readline()
		name = pointsfile.readline()
		try:
			wrong = int(pointsfile.readline())
		except:
			wrong = 0
		try:
			correct = int(pointsfile.readline())
		except:
			correct = 0
			correct = 0
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
			correct += 1
		else:
			print(name, "This is Wrong!")
			points = points-0.7
			wrong += 1
			wrong5 += 1
		if wrong5 == 5:
			wrong5 = 0
			print("Your session is ending as you have got too many wrong answers. Enter the code ", username, " when running this again.")
			break
	print("Your score is", points, "and you have a total of ", wrong, "wrong answers and", correct, "correct answers. Enter the code", username, "to start where you left off. \n Would you like to select another level? Enter yes or no")
	filename = username+".txt"
	output = open("c:\\Python\\MeanUsers\\"+filename, "w")
	output.write(str(points)+"\n"+name+"\n"+str(wrong)+"\n"+str(correct))
	output.close()
	choiceplay = input()
	if choiceplay == "Yes":
		print("You have selected yes, press enter to continue.")
	else:
		play = False
	input()