# Define a class for loan purpose selection
from enum import Enum


class Purpose(Enum):
    MORTGAGE = 1
    BUSINESS = 2
    CAR = 3
    CONSUMER = 4

# Define a base rate modifier for credit purpose selection
def modifier(key: Purpose):
    try:
        return {
            Purpose.MORTGAGE: -2,
            Purpose.BUSINESS: -0.5,
            Purpose.CAR: 0,
            Purpose.CONSUMER: 1.5
        }[key]
    except KeyError as e:
        return 0
