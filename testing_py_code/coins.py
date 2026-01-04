def get_coin_combination(cents: int) -> list:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins


def t_should_return_different_coins():
    result = get_coin_combination(6)
    if result[0] > 5 or result[1] > 10 or result[2] > 25:
        raise AssertionError()
    summa = result[0] + result[1] * 5 + result[2]*10 + result[3]*25
    if summa != 6:
        raise AssertionError()


t_should_return_different_coins()