import random
"""
1 = rock
0 = paper
-1 = scissor
"""
computer = random.choice ([1,0,-1])
yourchoice = input("enter your choice :")
youDict = {"r" : 1 ,"p" : 0 ,"s" : -1}
rev_Dict = {1 : "rock",0 : "paper",-1 : "scissor"}
if yourchoice not in youDict:
    print("enter your choice form p,r,s")
else:
  you = youDict[yourchoice]
  print(f"your chioce is {rev_Dict[you]}\n computer choice is {rev_Dict[computer]}")
  if (computer == you ):
        print("its a draw")
  else:
        if (computer == 1 and you  == 0):
            print("you win")
        elif (computer == 1 and you == -1):
            print("you lose")
        elif (computer == 0 and you == 1):
            print("you lose")
        elif (computer == 0 and you == -1):
            print("you win")
        elif (computer == -1 and you == 1):
            print("you win")
        elif (computer == -1 and you == 0):
            print("you lose")
        else:
            print("something went wrong")
   