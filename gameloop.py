from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR / 'resources'

with open(RESOURCES_DIR / 'players.json', 'rt') as fp:
    currentPlayerJson = json.loads(fp.read())

# currentPlayerJson = [] # For testing


class Player():
    def __init__(self, id: int):
        playerDict = next(
            (item for item in currentPlayerJson if item["id"] == id), None)
        if playerDict == None:
            raise ValueError("player id provided not found in list")
        self.raw_dict = playerDict
        self.id = playerDict['id']
        self.username = playerDict['username']
        self.score = 0

    def __str__(self):
        return(f"player with id '{self.id}', called '{self.username}' with score of '{self.score}'")

    def __repr__(self):
        return(f"Player(id={self.id})")


class Game():
    def __init__(self, *argv):
        self.players = argv
        self.round = 0
    
    def __str__(self):
        return(f"game in round {self.round} with players {', '.join([player.name for player in self.players])}")


p1 = Player(0)
p2 = Player(1)

g1 = Game(p1, p2)

print(g1.players[1].username)
print(g1)
