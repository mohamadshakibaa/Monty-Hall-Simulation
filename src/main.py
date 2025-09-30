import random


def monty_hall_game(switch_choice: bool) -> bool:
    """
    Simulate a single Monty Hall game.

    :param bool =switch_choice: If True, the contestant will switch their choice after a goat door is revealed.
    :return: True if the contestant won the car, False otherwise.
    :rtype: bool
    """
    # Initialize doors with one having a car and the rest goats
    doors = ["goat", "goat", "car"]

    random.shuffle(doors)

    # Contestant selects a door initially
    initial_choice = random.choice(range(len(doors)))

    # Monty reveals a door with a goat
    doors_revealed = [i for i in range(len(doors)) if i != initial_choice and doors[i] != "car"]
    door_revelead = random.choice(doors_revealed)

    # If contestant decides to switch, their final choice is the remaining door
    if switch_choice :
        finally_choice = [i for i in range(len(doors)) if i != door_revelead and i != initial_choice][0]
    else:
        # Keep the initial choice
        finally_choice = initial_choice
    
    # Return if contestant won the car
    return doors[finally_choice] == "car"
    
    
def simulate_game(number: int) -> None:
    """
    Simulate a number of Monty Hall games and print the statistics.

    :param int number: The number of games to simulate.
    :return: None
    """
    simulate_game_without_switch = sum([monty_hall_game(False) for _ in range(number)])
    simulate_game_with_switch = sum([monty_hall_game(True) for _ in range(number)])
    return simulate_game_without_switch, simulate_game_with_switch

print(simulate_game(100))
