import random
from typing import Generator


def dice_player(n_rounds: int) -> Generator[int, None, None]:
    for i in range(n_rounds):
        yield random.randint(1, 6)


def dice_game(n_rounds: int) -> str:
    player1 = dice_player(n_rounds)
    player2 = dice_player(n_rounds)
    player1_wins = 0
    player2_wins = 0
    for round in range(n_rounds):
        player1_dice = next(player1)
        player2_dice = next(player2)
        if player1_dice > player2_dice:
            player1_wins += 1
        elif player2_dice > player1_dice:
            player2_wins += 1
        print(player1_dice, player2_dice)
    if player1_wins > player2_wins:
        return "First"
    elif player2_wins > player1_wins:
        return "Second"
    else:
        return "Draw"

dice_game_result = dice_game(5)
print(dice_game_result)