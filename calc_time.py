# * Purpose
# * Take time in minutes and display hours and minutes
from math import trunc


def calculate_time(mins):
    """This function takes mins and returns hours and minutes"""
    hours = mins / 60  # take quotient
    rem_mins = mins % 60  # take remainder as minutes
    print(f"{trunc(hours)} hours and {rem_mins} minutes.")


# function call
calculate_time(79+54+60+25+60)
