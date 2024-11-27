import random

# Function to roll three dice
def roll_dice():
    return [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

# Function to calculate the score for a turn
def calculate_turn_score(dice):
    # Check if all dice are the same ("tuple out")
    if len(set(dice)) == 1:  # All three dice are the same
        print(f"Tuple out! {dice} - You score 0 points this turn.")
        return 0
    return sum(dice)

# Function to play a single turn for one player
def play_turn(current_player):
    print(f"\nPlayer {current_player + 1}'s turn!")
    dice = roll_dice()
    print(f"Rolled: {dice}")
    
    # Identify fixed and unfixed dice
    fixed = [die for die in dice if dice.count(die) > 1]
    unfixed = [die for die in dice if die not in fixed]

    # Loop until the player stops rerolling or all dice are fixed
    while unfixed:
        reroll_choice = input("Do you want to reroll unfixed dice? (y/n): ").lower()
        if reroll_choice == "n":
            break

        # Reroll only the unfixed dice
        new_rolls = [random.randint(1, 6) for _ in unfixed]
        dice = fixed + new_rolls
        print(f"New roll: {dice}")

        # Update fixed and unfixed dice
        fixed = [die for die in dice if dice.count(die) > 1]
        unfixed = [die for die in dice if die not in fixed]

        # Check for tuple out again after reroll
        if len(set(dice)) == 1:
            print(f"Tuple out! {dice} - You score 0 points this turn.")
            return 0

    # Calculate and return the final turn score
    turn_score = calculate_turn_score(dice)
    print(f"Turn over! Scored: {turn_score}")
    return turn_score

# Main Game Logic (Keeps Going Until One Player Wins)
# Initializing game variables
player_scores = [0, 0]
current_player = 0
target_score = 20

# Game begins
print("Starting Tuple Out Dice Game!")

# Keep playing until one player reaches the target score
while max(player_scores) < target_score:
    print(f"\nCurrent Scores: {player_scores}")
    turn_score = play_turn(current_player)  # Play turn for the current player
    player_scores[current_player] += turn_score  # Update the current player's score

    # Check if the current player has reached the target score
    if player_scores[current_player] >= target_score:
        print(f"\nPlayer {current_player + 1} wins with {player_scores[current_player]} points!")
        break

    # Switch to the next player
    current_player = (current_player + 1) % 2
