# Define a modifier for requested amount
import math


def modifier(requested_amount: float):
    if requested_amount < 1:
        return 0

    return -(math.log10(requested_amount))
