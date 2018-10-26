from sys import exit

def gold_room():
	print("This room is full of gold")

	choice = input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a numbher")

	if how_much<50:
		print("Nice you're not greedy")
		exit(0)
	else:
		dead("You greed y bastard")

def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")

	bear_moved = False

	if choice == "take honey":
		dead("The bear looks at you then slaps you face off")

	elif choice == "taunt bear" and not bear_moved:
		print("The bear has moved from the door")
		print("you can go thorugh now")
		bear_moved = True

	elif choice == "taunt bear" and bear_moved:
		dead("The bear kills")
	elif choice == "open door" and bear_moved:
		gold_room()
	else:
		print("I got no idea what error is this")


def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	choice = input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("well that was not good")
	else:
		cthulhu_room()


def dead(why):
	print(why, "good job")
	exit(0)

def start():


	choice = input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You will die of hunger")

start()