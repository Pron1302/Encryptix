#!/usr/bin/env python3

import random
X = '\033[0m'
Bold = '\033[1;36m'
HighB = '\033[1;44m'

winEas = loseEas = tieEas = winInt = loseInt = tieInt = winHard = loseHard = tieHard = winExp = loseExp = tieExp = winspec = losespec = tiespec = 0.0

hiddenfound = False

buildTMatrix = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
buildTMatrixL = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
buildTMatrixT = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}

n = 3
m = 3
tMatrix = [[0] * m for i in range(n)]
tMatrixL = [[0] * m for i in range(n)]
tMatrixT = [[0] * m for i in range(n)]

probabilitiesRPS = [1/3,1/3,1/3]

buildTMatrixrpsclsp = {'rr': 1, 'rp': 1, 'rsc': 1, 'rl': 1, 'rsp': 1, 'pr': 1, 'pp': 1, 'psc': 1, 'pl': 1, 'psp': 1, 'scr': 1, 'scp': 1, 'scsc': 1, 'scl': 1, 'scsp': 1, 'lr': 1, 'lp': 1, 'lsc': 1, 'll': 1, 'lsp': 1, 'spr': 1, 'spp': 1, 'spsc': 1, 'spl': 1, 'spsp': 1}
buildTMatrixLrpsclsp = {'rr': 1, 'rp': 1, 'rsc': 1, 'rl': 1, 'rsp': 1, 'pr': 1, 'pp': 1, 'psc': 1, 'pl': 1, 'psp': 1, 'scr': 1, 'scp': 1, 'scsc': 1, 'scl': 1, 'scsp': 1, 'lr': 1, 'lp': 1, 'lsc': 1, 'll': 1, 'lsp': 1, 'spr': 1, 'spp': 1, 'spsc': 1, 'spl': 1, 'spsp': 1}
buildTMatrixTrpsclsp = {'rr': 1, 'rp': 1, 'rsc': 1, 'rl': 1, 'rsp': 1, 'pr': 1, 'pp': 1, 'psc': 1, 'pl': 1, 'psp': 1, 'scr': 1, 'scp': 1, 'scsc': 1, 'scl': 1, 'scsp': 1, 'lr': 1, 'lp': 1, 'lsc': 1, 'll': 1, 'lsp': 1, 'spr': 1, 'spp': 1, 'spsc': 1, 'spl': 1, 'spsp': 1}

sheldon = 5
cooper = 5
tMatrixrpsclsp = [[0] * sheldon for i in range(cooper)]
tMatrixLrpsclsp = [[0] * sheldon for i in range(cooper)]
tMatrixTrpsclsp = [[0] * sheldon for i in range(cooper)]

probabilitiesrpsclsp = [1/5,1/5,1/5,1/5,1/5]
intro = """
Welcome to Rock Paper Scissors the Ultimate Version! There are four modes: Beginner, Intermediate, Expert, and Super Hard. Beginner is random, Intermediate uses AI, Expert uses Machine Learning, and Super Hard is... well... super hard. To play, type in the number corresponding to the command unless it asks for a yes or no answer. It's pretty self explanatory tbh so you should be fine.

Oh, and if you try to cheat off my code I WILL FIND YOU. Have fun!

P.S. There is a hidden mode that is pretty easy to figure out if you look at the code but thats no fun so try using your ingenuity to figure it out. Here's a hint: Bazinga!!!
"""
print(Bold)
print(intro)
print(X)

def chooseMode():
  mode = 6
  try:
    mode = int(input("What Mode do you want to play in? 1: beginner, 2: intermediate, 3: expert, or 4: super hard? Enter a number \n"))
  except ValueError:
    print("you must enter an integer \n")

  if(mode > 4 and mode != 73):
    print ("You must enter an integer less than five \n")
    while(mode > 4 and mode != 73):
      try:
        mode = int(input("What Mode do you want to play in? 1: begginner, 2: intermediate, 3: expert, or 4: super hard? Enter a number \n"))
      except ValueError:
        print("you must enter an integer \n")
  return mode

def easyMode():
  choices = ["Rock","Paper","Scissors"]
  continuePlaying = True
  continueGame = ""
  try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
  except ValueError:
    print("you must enter an integer \n")

  if(choice > 2 or choice < 0):
    print ("You must enter an integer less than three and greater than 0  \n")
    while(choice > 2 or choice < 0):
      print ("You must enter an integer less than three and greater than 0 \n")
      try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
      except ValueError:
        print("you must enter an integer \n")

  machineChoice = random.randint(0, 2)
  result = checkWin(choice,machineChoice,1)
  print ("You chose %s" % choices[choice])
  print ("The machine chose %s" % choices[machineChoice])
  print("You %s" % result)

  while(continuePlaying):
    try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
    except ValueError:
      print("you must enter an integer \n")

    if((choice > 2 or choice < 0) and choice != 5):
      print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.  \n")
      while((choice > 2 or choice < 0) and choice != 5):
        print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.\n")
        try:
          choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
        except ValueError:
          print("you must enter an integer \n")
    if (choice == 5):
      print ("Thanks for Playing!")
      continuePlaying = False
    else:
      machineChoice = random.randint(0, 2)
      result = checkWin(choice,machineChoice,1)

      print ("You chose %s" % choices[choice])
      print ("The machine chose %s" % choices[machineChoice])
      print("You %s" % result)

      #continueGame = input("Do you want to continue? Yes or No. \n")
      #while(continueGameCheck(continueGame) == "Wrong input"):
      #  continueGame = input("Do you want to continue? Yes or No. This time actually put in Yes or No... \n")

      #if (continueGame == "Yes"):
        #continuePlaying = True
      #else:
        #continuePlaying = False

def intermediateMode():
	choices = ["Rock", "Paper", "Scissors"]
	continuePlaying = True
	continueGame = ""
	prevChoice = ""
	prevMachineChoice = ""
	result = ""
	streak = 0
	won = 0
	alt = 0
	numoff = 0
	choice = 3

	try:
		choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
	except ValueError:
		print("you must enter an integer \n")

	if (choice > 2 or choice < 0):
		print(
		    "You must enter an integer less than three and greater than or equal to 0. \n")
		while (choice > 2 or choice < 0):
			try:
				choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
			except ValueError:
				print("you must enter an integer \n")
	machineChoice = random.randint(0, 2)
	result = checkWin(choice, machineChoice, 2)
	if (result == "Win!"):
		won += 1
	else:
		numoff += 1
		if (numoff == 3):
			won -= 3
			numoff = 0
		if (won < 0):
			won = 0

	print("You chose %s" % choices[choice])
	print("The machine chose %s" % choices[machineChoice])
	print("You %s" % result)

	prevChoice = choice
	prevMachineChoice = machineChoice
	streak += 1

	while (continuePlaying):
		try:
			choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
		except ValueError:
			print("you must enter an integer \n")

		if ((choice > 2 or choice < 0) and choice != 5):
			print(
			    "You must enter an integer less than three and greater than or equal to 0. Or put 5 to exit \n"
			)
			while ((choice > 2 or choice < 0) and choice != 5):
				try:
					print(
					    "You must enter an integer less than three and greater than or equal to 0. Or put 5 to exit \n"
					)
					choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
				except ValueError:
					print("you must enter an integer \n")

		if (choice == 5):
			print("Thanks for Playing!")
			continuePlaying = False
		else:
			if (prevChoice == choice):
				streak += 1
			else:
				streak -= 1
				if (streak < 0):
					streak = 0
			if (streak > 3):
				machineChoice = prevChoice - 2
				if (machineChoice < 0):
					machineChoice += 3
			elif (won > 9):
				print(
				    "Yo. Stop cheating and keep your eyes off my code. Just play normally. You wouldn't be able to look at previous decisions so accurately in a real game alright? If ya continue to do dis the machine won't care anymore - it's a sore loser and hates people like you."
				)
				machineChoice = random.randint(0, 2)
			elif (won > 3 and won < 10):
				machineChoice = prevChoice
			else:
				if (result == "Win!"):
					machineChoice = prevChoice - 2
					if (machineChoice < 0):
						machineChoice += 3
				elif (result == "Lose!"):
					machineChoice = prevChoice + 1
					if (machineChoice > 2):
						machineChoice -= 3
					machineChoice -= 2
					if (machineChoice < 0):
						machineChoice += 3
				else:
					machineChoice = random.randint(0, 2)

			result = checkWin(choice, machineChoice, 2)

			if (result == "Win!"):
				won += 1
			else:
				won -= 2
				if (won < 0):
					won = 0

			print("You chose %s" % choices[choice])
			print("The machine chose %s" % choices[machineChoice])
			print("You %s" % result)
			prevChoice = choice

def expertMode():
  global probabilitiesRPS
  choices = ["Rock","Paper","Scissors"]
  choi = ['r','p','s']
  continuePlaying = True
  prevChoice = ""
  choice = 3
  probRock = 0
  probPaper = 0
  probScissors = 0

  try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
  except ValueError:
    print("you must enter an integer \n")

  if((choice > 2 or choice < 0)):
    print ("You must enter an integer less than three and greater than or equal to 0  \n")
    while((choice > 2 or choice < 0)):
      print ("You must enter an integer less than three and greater than or equal to 0 \n")
      try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
      except ValueError:
        print("you must enter an integer \n")

  machineChoice = random.randint(0, 2)
  result = checkWin(choice,machineChoice,3)
  print ("You chose %s" % choices[choice])
  print ("The machine chose %s" % choices[machineChoice])
  print("You %s" % result)

  prevChoice = choice

  while(continuePlaying):
    choice = 3
    try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
    except ValueError:
      print("you must enter an integer \n")

    if((choice > 2 or choice < 0) and choice != 5):
      print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.  \n")
      while((choice > 2 or choice < 0) and choice != 5):
        print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.\n")
        try:
          choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
        except ValueError:
          print("you must enter an integer \n")
    if (choice == 5):
      print("Thanks for Playing!\n")
      continuePlaying = False
    else:
      transMatrix = buildTransitionProbabilities(prevChoice,choice,result)
      machineChoice = random.randint(1, 100)
      probabilitiesRPS[0] = transMatrix[prevChoice][0]
      probabilitiesRPS[1] = transMatrix[prevChoice][1]
      probabilitiesRPS[2] = transMatrix[prevChoice][2]
      rangeR = probabilitiesRPS[0] * 100
      rangeP = probabilitiesRPS[1] * 100 + rangeR
      if (machineChoice <= rangeR):
        machineChoice = 1
      elif (machineChoice <= rangeP):
        machineChoice = 2
      else:
        machineChoice = 0

      result = checkWin(choice,machineChoice,3)
      prevChoice = choice
      print ("You chose %s" % choices[choice])
      print ("The machine chose %s" % choices[machineChoice])
      print("You %s" % result)

  #print("Your winning transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrix[0],tMatrix[1],tMatrix[2]))
  #print("Your losing transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrixL[0],tMatrixL[1],tMatrixL[2]))
  #print("Your tying transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrixT[0],tMatrixT[1],tMatrixT[2]))

def buildTransitionProbabilities(pC,c,winloss):
  global buildTMatrix
  global buildTMatrixL
  global buildTMatrixT
  choi = ['r','p','s']

  if winloss == "Win!":
    for i, x in buildTMatrix.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrix['%s%s' % (choi[pC], choi[c])] += 1
  elif winloss == "Tied!":
    for i, x in buildTMatrixT.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrixT['%s%s' % (choi[pC], choi[c])] += 1
  else:
    for i, x in buildTMatrixL.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrixL['%s%s' % (choi[pC], choi[c])] += 1

  return buildTransitionMatrix(winloss)

def buildTransitionMatrix(winlosstwo):
  global tMatrix
  global tMatrixL
  global tMatrixT

  if winlosstwo == "Win!":
    rock = buildTMatrix['rr'] + buildTMatrix['rs'] +buildTMatrix['rp']
    paper = buildTMatrix['pr'] + buildTMatrix['ps'] +buildTMatrix['pp']
    scissors = buildTMatrix['sr'] + buildTMatrix['ss'] +buildTMatrix['sp']
    choi = ['r','p','s']
    for row_index, row in enumerate(tMatrix):
      for col_index, item in enumerate(row):
          a = int(buildTMatrix['%s%s' % (choi[row_index],choi[col_index])])
          if (row_index == 0):
            c = a/rock
          elif (row_index == 1):
            c = a/paper
          else:
            c = a/scissors
          row[col_index] = float(c)
    return (tMatrix)
  elif winlosstwo == "Tied!":
    rock = buildTMatrixT['rr'] + buildTMatrixT['rs'] +buildTMatrixT['rp']
    paper = buildTMatrixT['pr'] + buildTMatrixT['ps'] +buildTMatrixT['pp']
    scissors = buildTMatrixT['sr'] + buildTMatrixT['ss'] +buildTMatrixT['sp']
    choi = ['r','p','s']
    for row_index, row in enumerate(tMatrixT):
      for col_index, item in enumerate(row):
          a = int(buildTMatrixT['%s%s' % (choi[row_index],choi[col_index])])
          if (row_index == 0):
            c = a/rock
          elif (row_index == 1):
            c = a/paper
          else:
            c = a/scissors
          row[col_index] = float(c)
    return (tMatrixT)

  else:
    rock = buildTMatrixL['rr'] + buildTMatrixL['rs'] +buildTMatrixL['rp']
    paper = buildTMatrixL['pr'] + buildTMatrixL['ps'] +buildTMatrixL['pp']
    scissors = buildTMatrixL['sr'] + buildTMatrixL['ss'] +buildTMatrixL['sp']
    choi = ['r','p','s']
    for row_index, row in enumerate(tMatrixL):
      for col_index, item in enumerate(row):
          a = int(buildTMatrixL['%s%s' % (choi[row_index],choi[col_index])])
          if (row_index == 0):
            c = a/rock
          elif (row_index == 1):
            c = a/paper
          else:
            c = a/scissors
          row[col_index] = float(c)
    return (tMatrixL)
def superHard():
  choices = ["Rock","Paper","Scissors"]
  continuePlaying = True
  continueGame = ""
  result = ""
  print ("I am going to play %s" % choices[random.randint(0, 2)])
  try:
    choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
  except ValueError:
    print("you must enter an integer \n")

  if((choice > 2 or choice < 0)):
    print ("You must enter an integer less than three and greater than or equal to 0 \n")
    while((choice > 2 or choice < 0)):
      try:
        print ("You must enter an integer less than three and greater than or equal to 0 \n")
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
      except ValueError:
        print("you must enter an integer \n")

  machineChoice = choice - 2
  if (machineChoice < 0):
    machineChoice += 3

  result = checkWin(choice,machineChoice,4)
  print ("You chose %s" % choices[choice])
  print ("The machine chose %s" % choices[machineChoice])
  print("You %s" % result)

  while(continuePlaying):
    print ("I am going to play %s" % choices[random.randint(0, 2)])
    try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
    except ValueError:
      print("you must enter an integer \n")

    if((choice > 2 or choice < 0) and choice != 5):
      print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit. \n")
      while((choice > 2 or choice < 0) and choice != 5):
        try:
          print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit. \n")
          choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
        except ValueError:
          print("you must enter an integer \n")

    if (choice == 5):
      print("Giving up? How sad :(")
      continuePlaying = False
    else:
      machineChoice = choice - 2
      if (machineChoice < 0):
        machineChoice += 3

      result = checkWin(choice,machineChoice,4)
      print ("You chose %s" % choices[choice])
      print ("The machine chose %s" % choices[machineChoice])
      print("You %s" % result)

def bigbang():
  global hiddenfound
  global probabilitiesRPS
  choices = ["Rock","Paper","Scissors","Lizard","Spock"]
  choi = ['r','p','sc','l','sp']
  continuePlaying = True
  prevChoice = ""
  choice = 8
  probRock = 0
  probPaper = 0
  probScissors = 0
  probLizard = 0
  probSpock = 0

  try:
    choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock \n"))
  except ValueError:
    print("you must enter an integer \n")

  if((choice > 4 or choice < 0)):
    print ("You must enter an integer less than five and greater than or equal to 0  \n")
    while((choice > 4 or choice < 0)):
      print ("You must enter an integer less than five and greater than or equal to 0 \n")
      try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock \n"))
      except ValueError:
        print("you must enter an integer \n")

  machineChoice = random.randint(0, 4)
  result = checkWin(choice,machineChoice,73)
  print ("You chose %s" % choices[choice])
  print ("The machine chose %s" % choices[machineChoice])
  print("You %s" % result)

  prevChoice = choice

  while(continuePlaying):
    choice = 8
    try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock, 7: exit \n"))
    except ValueError:
      print("you must enter an integer \n")

    if((choice > 4 or choice < 0) and choice != 7):
      print ("You must enter an integer less than five and greater than or equal to 0 or choose 5 to exit.  \n")
      while((choice > 4 or choice < 0) and choice != 7):
        print ("You must enter an integer less than five and greater than or equal to 0 or choose 5 to exit.\n")
        try:
          choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock, 7: exit \n"))
        except ValueError:
          print("you must enter an integer \n")
    if (choice == 7):
      hiddenfound = True
      print ("\033[1;36m\nThere's just no pleasing you, is there, Leonard?" + X)
      continuePlaying = False
    else:
      transMatrix = buildTransitionProbabilitiesrpsclsp(prevChoice,choice,result)
      machineChoice = random.randint(1, 100)
      probabilitiesrpsclsp[0] = transMatrix[prevChoice][0]
      probabilitiesrpsclsp[1] = transMatrix[prevChoice][1]
      probabilitiesrpsclsp[2] = transMatrix[prevChoice][2]
      probabilitiesrpsclsp[3] = transMatrix[prevChoice][3]
      probabilitiesrpsclsp[4] = transMatrix[prevChoice][4]
      rangeR = probabilitiesrpsclsp[0] * 100
      rangeP = probabilitiesrpsclsp[1] * 100 + rangeR
      rangeSC = probabilitiesrpsclsp[2] * 100 + rangeP
      rangeL = probabilitiesrpsclsp[3] * 100 + rangeSC
      oneOrTwo = random.randint(1,2)
      if (machineChoice <= rangeR):
          if (oneOrTwo == 1):
              machineChoice = 1
          else:
              machineChoice = 4
      elif (machineChoice <= rangeP):
          if (oneOrTwo == 1):
              machineChoice = 2
          else:
              machineChoice = 3
      elif (machineChoice <= rangeSC):
          if (oneOrTwo == 1):
              machineChoice = 4
          else:
              machineChoice = 0
      elif (machineChoice <= rangeL):
          if (oneOrTwo == 1):
              machineChoice = 2
          else:
              machineChoice = 0
      else:
          if (oneOrTwo == 1):
              machineChoice = 1
          else:
              machineChoice = 3
      result = checkWin(choice,machineChoice,73)
      prevChoice = choice
      print ("You chose %s" % choices[choice])
      print ("The machine chose %s" % choices[machineChoice])
      print("You %s" % result)

  #print("Your winning transition matrix is:\nr: %s\np: %s\nsc: %s\nl: %s\nsp: %s\n" % (tMatrixrpsclsp[0],tMatrixrpsclsp[1],tMatrixrpsclsp[2],tMatrixrpsclsp[3],tMatrixrpsclsp[4]))
  #print("Your losing transition matrix is:\nr: %s\np: %s\nsc: %s\nl: %s\nsp: %s\n" % (tMatrixLrpsclsp[0],tMatrixLrpsclsp[1],tMatrixLrpsclsp[2],tMatrixLrpsclsp[3],tMatrixLrpsclsp[4]))
  #print("Your tying transition matrix is:\nr: %s\np: %s\nsc: %s\nl:
