# Define a class for income source selection
from enum import Enum


class IncomeSource(Enum):
    PASSIVE = 1
    HIRED = 2
    OWNER = 3
    UNEMPLOYED = 4


def modifier(key: IncomeSource):
    try:
        return {
            IncomeSource.PASSIVE: 0.5,
            IncomeSource.HIRED: -0.25,
            IncomeSource.OWNER: 0.25,
            IncomeSource.UNEMPLOYED: 0
        }[key]
    except KeyError as e:
        return 0

def max_requested_amount(key: IncomeSource):
    try:
        return {
            IncomeSource.PASSIVE: 1000000,
            IncomeSource.HIRED: 5000000,
            IncomeSource.OWNER: 10000000,
            IncomeSource.UNEMPLOYED: 0
        }[key]
    except KeyError as e:
        return 0
