import gameloop
import UserSystem

def choose_player(player):
	user = UserSystem.get_user(name=input(f"Enter player {player}'s username: "))
	while user == None:
		user = UserSystem.get_user(name=input(f"Enter player {player}'s username: "))
	return(user["id"])


while True:
	choice = input("\u0332".join("	Dice Game Main Menu ") + """
	1: Display rules
	2: Play a game
	3: Create User
	4: Quit

	Please enter your choice: """)

	if choice == "1":
		print("\u0332".join("	Dice Game Rules ") +
		"""
	This is a 2 player game
	The active player throws 2 dice
	The value of the throw is added to your score
	You can have as many throws as you want until you decide to pass the dice or you throw a double
	If the throw is a double, your score is set to 0 and your turn ends
	The first player to reach a score of 50 wins.
		""")
		print()
		input("Press enter to go to back to main menu.")
	elif choice == "2":
		gameloop.game(choose_player("one"), choose_player("two"))
	elif choice == "3":
		user_created = UserSystem.create_user(input("Enter the username to create a player with: "))
		while user_created == False:
			user_created = UserSystem.create_user(input("Enter the username to create a player with: "))
	elif choice=="4":
		exit()
	else:
		print("Please enter 1 ,2 or 3")