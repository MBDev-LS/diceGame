import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR / 'resources'

with open(RESOURCES_DIR / 'system.json','rt') as fp:
    system = json.loads(fp.read())

with open(RESOURCES_DIR / 'players.json','rt') as fp:
    players = json.loads(fp.read())

def post_user(id: int, won: bool):
    print(id)
    print(won)
    with open(RESOURCES_DIR / 'players.json','rt') as fp:
        players = json.loads(fp.read())
    player = next((item for item in players if item["id"] == id), None)
    print(players, player)
    if player:
        player["games_played"] += 1
        if won:
            player["games_won"] += 1
        with open(RESOURCES_DIR / 'players.json','wt') as fp:
            fp.write(json.dumps(players))
        print(players, player)
        return True
    return False



def get_user(name: str=None, id: int=None, password: bool=False):
    with open(RESOURCES_DIR / 'players.json','rt') as fp:
        players = json.loads(fp.read())
    if name:
        return next((item for item in players if item["username"] == name), None)
    elif id:
        return next((item for item in players if item["id"] == id), None)

def create_user(username: str):
    if get_user(name=username) is not None:
        return False
    user_dict = {"id":system["NextID"], "username":username, "games_played":0, "games_won":0}
    players.append(user_dict)
    system["NextID"] += 1
    with open(RESOURCES_DIR / 'players.json','wt') as fp:
        fp.write(json.dumps(players))
    with open(RESOURCES_DIR / 'system.json','wt') as fp:
        fp.write(json.dumps(system))
    return(user_dict)