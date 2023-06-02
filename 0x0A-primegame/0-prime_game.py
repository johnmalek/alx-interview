#!/usr/bin/python3
"""
A python module to find the winner of a prime game
"""

def is_prime(number):
    """
    Check if a number is prime or not
    args:
        number - number to be checked
    Returns:
        True if number is prime
        False if number is not prime
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def isWinner(x, numbers):
    person1_wins = 0
    person2_wins = 0

    for num in numbers:
        prime_numbers = [i for i in range(2, num + 1) if is_prime(i)]
        person1_turn = True

        while prime_numbers:
            prime_number = prime_numbers.pop(0)
            multiples = [i for i in range(prime_number, num + 1, prime_number)]
            prime_numbers = [p for p in prime_numbers if p not in multiples]

            if person1_turn:
                person1_turn = False
            else:
                person1_turn = True

        if person1_turn:
            person2_wins += 1
        else:
            person1_wins += 1

    if person1_wins > person2_wins:
        return 'Maria'
    elif person2_wins > person1_wins:
        return 'Ben'
    else:
        return None
