"""
MCS 260 Project One by Rafeh Qazi
Modified: September 2016
Program: Calculate drainage time
"""
import math

# Gravity constant
G = 9.80665

# Welcome prompt

# Take in user input
def user_input():
    a = float(input('Give the cross-sectional area of the hole the liquid is draining out of: '))
    A = float(input('Give the horizontal cross-sectional area of the container: '))
    H = float(input('Give the height of the liquid above the hole it is draining out of: '))

# Drain time formula
def drain_time_secs(a, A, H):
    return ((2 * A) / a) * math.sqrt((2 * H) / G)

# Use divmod to get quotient and remainder
def calculate(drain_time_secs):
    minutes, seconds = divmod(drain_time_secs, 60)
    hours, minutes = divmod(minutes, 60)

    # Handle all string formatting cases of having seconds, minutes, or hours.
    if seconds and minutes and hours:
        return '{} hours {} minutes and {} seconds'.format(int(hours), int(minutes), int(seconds))

    elif seconds and minutes:
        return '{} minutes and {} seconds'.format(int(minutes), int(seconds))

    elif minutes and hours:
        return '{} hours and {} minutes'.format(int(hours), int(minutes))

    elif seconds and hours:
        return '{} hours and {} seconds'.format(int(hours), int(seconds))

    elif hours:
        return '{} hours'.format(int(hours))

    elif minutes:
        return '{} minutes'.format(int(minutes))

    elif seconds:
        return '{} seconds'.format(int(seconds))


if __name__ == '__main__':
    print('Hello, welcome to my drain time calculator!')
    pass