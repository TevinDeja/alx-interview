#!/usr/bin/python3
"""
Module for makeChange function
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list of int): List of coin denominations available.
    total (int): The target amount.

    Returns:
    int: Fewest number of coins needed to meet total, or -1 if not possible.
    """
     if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
