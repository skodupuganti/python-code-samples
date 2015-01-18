#Purpose of this program is to simulate Rock Paper Scissor Lizard Spock game.
#More info about game can be found in wikipedia
import random

#Convert name to number
def name_to_number(name):
	if(name=="rock"):
		number=0
	elif(name=="spock"):
		number=1
	elif(name=="paper"):
		number=2
	elif(name=="lizard"):
		number=3
	elif(name=="scissors"):
		number=4
	else:
		print "Wrong name"
	return number

#Convert number to name
def number_to_name(number):
	if(number==0):
		name="rock"
	elif(number==1):
		name="spock"
	elif(number==2):
		name="paper"
	elif(number==3):
		name="lizard"
	elif(number==4):
		name="scissors"
	else:
		print "Wrong number"
	return name

#Determine winner and print
def rpsls(player_choice):
	comp_num=random.randrange(0,5)
	player_num=name_to_number(player_choice)
	comp_choice=number_to_name(comp_num)
	#Difference of numbers modulo 5, each number wins with preceeding two and loses to next two in terms of numbers when taken on a circle
	decision=(player_num-comp_num)%5
	#determine winner and print values
	if decision in [1,2]:
		win = "Player Wins"
	elif decision == 0:
		win = "Player and Computer Tie"
	else:
		win = "Computer Wins"
	print "Player chooses " + player_choice
	print "Computer chooses " + comp_choice
	print win
	print "\n\n"

#test code
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
