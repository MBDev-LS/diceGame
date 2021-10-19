import random
import time

{
			"dice_results": [2, 5],
			"new_points": 7,
			"double": False,
		}

def roll():
    points = 0
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    dietotal = die1 + die2
    points = points + dietotal

    if die1 == die2:
        points = 0

    return {
        "dice_results": [die1, die2],
        "new_points": points,
        "double": True if die1 == die2 else False,
    }

def main():
    user1 = ("Bob")
    user2 = ("Jeff")

    i = 0
    Player1Points = 0
    Player2Points = 0
    Player1Tiebreaker = 0
    Player2Tiebreaker = 0
    Winner_Points = 0

    for i in range(1,5):
        Player1Points += roll()
        print('After this round ',user1, 'you now have: ',Player1Points,' points')
        time.sleep(1)
        Player2Points += roll()
        print('After this round ',user2, 'you now have: ',Player2Points,' points')
        time.sleep(1)

    if Player1Points == Player2Points:
        while Player1Tiebreaker == Player2Tiebreaker:

            Player1Tiebreaker = random.randint(1,6)
            Player2Tiebreaker = random.randint(1,6)

        if Player1Tiebreaker > Player2Tiebreaker:
            Player1Points = 50
        elif Player2Tiebreaker > Player1Tiebreaker:
            Player2Points = 50

    if Player1Points > 49:
        Winner_Points = Player1Points
        winner_User = user1
        winner = (Winner_Points, user1)
    elif Player2Points > 49:
        Winner_Points = Player2Points
        winner_User = user2
        winner = (Winner_Points, user2)

    print('Well done, ', winner_User,' you won with ',Winner_Points,' points')

if __name__ == "__main__":
    main()