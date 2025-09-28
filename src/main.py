import random


def monty_hall_game(switch_choice: bool) -> bool:
    doors = ["goat", "goat", "car"]

    random.shuffle(doors)

    initial_choice = random.choice(range(len(doors)))

    doors_revealed = [i for i in range(len(doors)) if i != initial_choice and doors[i] != "car"]
    door_revelead = random.choice(doors_revealed)

    if switch_choice :
        finally_choice = [i for i in range(len(doors)) if i != door_revelead and i != initial_choice][0]
    else:
        finally_choice = initial_choice
    
    return doors[finally_choice] == "car"
    
    
def simulate_game(number):
    simulate_game_without_switch = sum([monty_hall_game(False) for _ in range(number)])
    simulate_game_with_switch = sum([monty_hall_game(True) for _ in range(number)])
    return simulate_game_without_switch, simulate_game_with_switch

print(simulate_game(100))
