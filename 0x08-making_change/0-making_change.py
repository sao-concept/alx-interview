#!/usr/bin/python3
""" Making change """

def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total.

    Parameters:
    coins (list): List of coin denominations.
    total (int): Total amount to make change for.

    Returns:
    int: The fewest number of coins needed, or -1 if it's not possible to make the total.
    """

    # If the total is less than or equal to 0, no change needed.
    if total <= 0:
        return 0
    else:
        # Importing 'trunc' function from math module.
        from math import trunc

        # Sort coins in descending order for optimized calculation.
        coins = sorted(coins, reverse=True)
        # Dictionary to store the count of each coin denomination.
        coin_dict = {}

        # Loop until total is not None.
        while total is not None:
            # Iterate through each coin denomination.
            for c in coins:
                # Check if total can be divided evenly by the current coin denomination.
                if total % c == 0:
                    # Store the count of coins needed for the denomination.
                    coin_dict[c] = total / c
                    # Return the total number of coins needed.
                    return(int(sum(coin_dict.values())))
                else:
                    # Store the count of coins needed for the denomination, truncating the float division.
                    coin_dict[c] = trunc(total / float(c))
                    # Update the remaining total after considering the current coin denomination.
                    total -= (c * coin_dict[c])
            # If it's not possible to make the total with given coins, return -1.
            return -1
