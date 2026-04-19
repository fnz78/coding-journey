import math


def bulb_switch(n: int) -> int:
    """
    Returns number of bulbs that remain ON after n rounds.
    """
    return int(math.sqrt(n))


if __name__ == "__main__":
    n = int(input("Enter number of bulbs: "))
    print("Bulbs ON:", bulb_switch(n))
