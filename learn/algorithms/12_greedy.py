"""
Greedy algorithms make the locally optimal choice at each step with the hope of finding a global optimum.
They are simple to implement and efficient for problems like the Coin Change problem (with standard denominations).
"""


def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count if amount == 0 else -1


if __name__ == "__main__":
    print(f"Coins: {coin_change([1, 5, 10, 25], 63)}")
