from pathlib import Path
import json

import UserSystem
import dicesim

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR / 'resources'

with open(RESOURCES_DIR / 'players.json', 'rt') as fp:
	currentPlayerJson = json.loads(fp.read())


class Player():
	def __init__(self, player_id: int):
		playerDict = next(
			(item for item in currentPlayerJson if item["id"] == player_id), None)
		if playerDict is None:
			raise ValueError("player id provided not found in list")
		self.raw_dict = playerDict
		self.player_id = playerDict['id']
		self.username = playerDict['username']
		self.score = 0

	def __str__(self):
		return f"player with id '{self.player_id}', called '{self.username}' with score of '{self.score}'"

	def __repr__(self):
		return f"Player(id={self.player_id})"

	def roll_dice(self):
		"""
		Calls dice simulation module to roll dice and returns a
		dictionary in the following format:
		{
			"dice_results": [1-6, 1-6],
			"new_points": int,
			"double": bool,
		}
		"""
		return dicesim.roll()


class Game():
	def __init__(self, *argv):
		if len(argv) > 2 or len(argv) == 0:
			raise ValueError(
				f"2 players must be given when intisialising a Game() object, not {len(argv)}")
		elif type(argv[0]) != Player or type(argv[1]) != Player:
			raise TypeError(f"players pass given when intisialising a Game() object must both be type {Player}, not {type(argv[0])} and {type(argv[1])}")

		self.players = argv
		self.round = 0
		self.user_round = 1

	def __str__(self):
		return f"game in round {self.round} with players {', '.join([player.username for player in self.players])}"

	def __repr__(self):
		return f"Game({repr(self.players[0])}, {repr(self.players[1])})"

	def start_turn(self, player_index: int):
		"""
		Takes in either 0 or 1 to denote the player whose
		turn is starting. It will then carry out the player's
		turn and return the resulting score increase.
		"""
		if type(player_index) != int:
			raise TypeError(
				f"player_index must be a int, not {type(player_index)}")
		if player_index != 0 and player_index != 1:
			raise ValueError(
				f"player_index must be 0 or 1, not {player_index}")

		new_points = 0

		print(f"It is now {self.players[player_index].username}'s turn!")

		while True:
			input("Press enter to roll!")

			roll_result = self.players[player_index].roll_dice()
			if roll_result['double'] is True:
				print(
					f"You have rolled a double of {roll_result['dice_results'][0]} and {roll_result['dice_results'][1]}, your turn is over and you gain 0 points!")
				return 0
			elif new_points >= 50:
				return new_points

			new_points += roll_result['new_points']
			print(
				f"You got {roll_result['dice_results'][0]} and {roll_result['dice_results'][1]} for a total of {roll_result['new_points']}!")

			playAgain = input('Would you like to roll again (y/n): ').lower()
			while playAgain != 'y' and playAgain != 'n':
				playAgain = input(
					'Would you like to play again (y/n): ').lower()
			if playAgain == 'n':
				print(
					f"Alright, your turn has ended and you scored a total of {new_points} this round!")
				return new_points


def game(player1_id: int, player2_id: int):
    """
    Takes in two player_ids and completes a game
    using their infomation stored in the player.json
    file. Then saves the game's result using the saving
    module and returns None to theMain Menu file.
    """
    p1 = Player(player1_id)
    p2 = Player(player2_id)

    game = Game(p1, p2)

    print(f"Welcome to the game, {p1.username} and {p2.username}!")
    input(f'{p1.username} will go first, press enter to start.')

    currentPlayer = 0

    while True:
        game.round += 1
        if currentPlayer == 1:
            game.user_round += 1

        print(f"\nWelcome to Round {game.user_round}")
        game.players[currentPlayer].score = game.start_turn(currentPlayer)

        if game.players[currentPlayer].score >= 50:
            print(f"{game.players[currentPlayer].username} won!")
            post1 = UserSystem.post_user(game.players[currentPlayer].player_id, True)
            post2 = UserSystem.post_user(game.players[1 if currentPlayer == 0 else 0].player_id, False)

            if not post1 is True or not post2 is True:
                print("Error saving data.")

            # This will be changed to saving the game to the player's data and returning to the main menu module.
            break
		
        currentPlayer = 1 if currentPlayer == 0 else 1

if __name__ == "__main__":
	game(0, 1)