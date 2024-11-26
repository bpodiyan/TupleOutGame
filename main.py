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
