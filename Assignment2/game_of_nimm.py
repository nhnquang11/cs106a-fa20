"""
File: game_of_nimm.py
-------------------------
Game of Nim:
    1 - The game starts with a pile of 20 stones between the players
    2 - The two players alternate turns
    3 - On a given turn, a player may take either 1 or 2 stone from the center pile
    4 - The two players continue until the center pile has run out of stones.
"""

def main():
    num_stones = 20
    player_turn = 1
    while num_stones > 0:
        print(f"There are {num_stones} stones left")
        stones_removed = get_stones_input(player_turn)
        num_stones -= stones_removed
        player_turn = next_turn(player_turn)
    print(f"Player {player_turn} wins!")

def get_stones_input(player_turn):
    """
    Repeatedly prompts user input for number of stones to remove until getting the valid one.
    """
    num_stones = int(input(f"Player {player_turn} would you like to remove 1 or 2 stones? "))
    while not (num_stones == 1 or num_stones == 2):
        num_stones = int(input("Please enter 1 or 2: "))
    return num_stones

def next_turn(turn):
    """
    Returns the next player turn given the current turn.
    """
    return 2 if turn == 1 else 1

if __name__ == '__main__':
    main()
