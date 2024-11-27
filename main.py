import random

class TupleOutDiceGame:
    def __init__(self, players=2, target_score=50):
        """
        Initializes the game settings, including the number of players, the target score for winning,
        and the starting scores for each player. Also sets the first player to take a turn.
        """
        self.players = players  # Number of players
        self.target_score = target_score  # Target score to win the game
        self.scores = [0] * players  # Scores for each player
        self.current_player = 0  # Start with Player 1

    def roll_dice(self):
       """
       This function is for simulating rolling three dice. The function returns a list of three random integers between 1 and 6.
       """
       return [random.randint(1, 6) for _ in range(3)]
    
    def play_turn(self):
       """
       Handles a single turn for the current player. Rolls dice, checks for "tuple out" (all dice are the same),
       allows the player to reroll unfixed dice, and calculates the turn score. Returns the score for the turn.
       """
       print(f"\nPlayer {self.current_player + 1}'s turn!")  # Indicate whose turn it is
       dice = self.roll_dice()  # Roll three dice initially
       print(f"Rolled: {dice}")  # Display initial roll


       while True:
           # Check if all dice are the same (tuple out)
           if len(set(dice)) == 1:
               print(f"Tuple out! {dice} - You score 0 points this turn.")  # Notify of tuple out
               return 0


           # Fix dice that have matching values
           fixed = [die for die in dice if dice.count(die) > 1]  # Fixed dice: any dice appearing more than once
           unfixed = [die for i, die in enumerate(dice) if die not in fixed or dice.count(die) == 1]  # Unfixed dice
           print(f"Fixed dice: {fixed}")  # Display fixed dice


           if not unfixed:  # If no unfixed dice remain, stop rerolling
               break


           # Ask the player if they want to reroll unfixed dice
           choice = input("Do you want to reroll unfixed dice? (y/n): ").lower()
           if choice != 'y':  # Stop if the player doesn't want to reroll
               break


           # Reroll only the unfixed dice
           new_rolls = [random.randint(1, 6) for _ in unfixed]  # Reroll unfixed dice
           dice = fixed + new_rolls  # Combine fixed dice with new rolls
           print(f"New roll: {dice}")  # Display updated dice roll


       turn_score = sum(dice)  # Calculate the score from all dice
       print(f"Turn over! Scored: {turn_score}")  # Display the final turn score
       return turn_score

