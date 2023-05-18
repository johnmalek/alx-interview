#!/usr/bin/python3
"""A python module
"""
import sys


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed to
    meet a given amount total
    args:
        coins: list of coins(denominations) available
        total: the total made from fewest coins possible
    Return: Int - few coins to make total
    """
    dp = [float('inf')] * (total +1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
            dp[i] = -1
    
    return dp[total]
