#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n: int) -> int:
    """
    In a text file, there is a single character H. Your text editor can execute
    only two operations in this file: Copy All and Paste. Given a number n,
    write a method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    Returns an integer
    If n is impossible to achieve, returns 0
    """
    if not isinstance(n, int) or n <= 0:
        return 0

    operations = 0
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
            divisor = 1
        divisor += 1
    return operations


# Example usage:
if __name__ == "__main__":
    n = 9
    print(minOperations(n))  # Output: 6
