# Define a modifier for credit score selection


def modifier(key: int):
    try:
        return {
            -2: 0,
            -1: 1.5,
            0: 0,
            1: -0.25,
            2: -0.75
        }[key]
    except KeyError as e:
        return 0

def max_requested_amount(key: int):
    try:
        return {
            -2: 0,
            -1: 1000000,
            0: 5000000,
            1: 10000000,
            2: 10000000
        }[key]
    except KeyError as e:
        return 0
