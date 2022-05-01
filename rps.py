import random

# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round.

moves = ['rock', 'paper', 'scissors']

# The Player class is the parent class for all of the Players
# in this game


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    # Setup subclass to inheirt the parent class and to
    # create any unique instance variables.
    # def __init__(self):
    #    super().__init__()

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(RandomPlayer):

    def move(self):

        while True:
            choice = input("rock, paper, scissors? ")
            if choice in moves:
                return choice

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):

    def __init__(self):
        self.p1_last_move = ""
        self.p2_last_move = ""

    def learn(self, p1_move, p2_move):

        self.p1_last_move = p1_move
        self.p2_last_move = p2_move

    def move(self):

        if self.p2_last_move != "":
            # if there is a last move, return last move for ReflectionPlayer
            return self.p2_last_move
        else:
            # else return random choice of moves.
            return random.choice(moves)


class CyclePlayer(Player):

    def __init__(self):
        self.p1_last_move = ""
        self.p2_last_move = ""

    def learn(self, p1_move, p2_move):

        self.p1_last_move = p1_move
        self.p2_last_move = p2_move

    def move(self):

        if self.p1_last_move == "":
            # if there is no last move, return a random move
            return random.choice(moves)
        else:
            # else cycle through moves and pick the next one
            if moves[0] == self.p1_last_move:
                return moves[1]
            elif moves[1] == self.p1_last_move:
                return moves[2]
            elif moves[2] == self.p1_last_move:
                return moves[0]
            else:
                print("shuld not get here...")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.ties = 0
        self.rounds = 5

    def who_won(self, move1, move2):

        # see if it's a tie and then
        # print who won or whether there was a tie.
        if move1 == move2:
            print("Its'a tie!")
            self.ties += 1
        else:
            # Call beats to see who won
            if beats(move1, move2) is True:
                print("Player 1 won!")
                self.p1_score += 1
            elif beats(move1, move2) is False:
                print("Player 2 won!")
                self.p2_score += 1
        print(f'''\nCumulative scores this round are Player1: {self.p1_score}
              Player2: {self.p2_score}
              and ties: {self.ties}!\n''')

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        # Check who won or whether there's a tie.
        self.who_won(move1, move2)
        # Remember what happend for next round
        self.p1.learn(move1, move2)
        # Removed second learn call
        # self.p2.learn(move2, move1)

    def play_game(self):

        print("Game start!\n")
        for round in range(self.rounds):
            # print the round number starting at one to be more user friendly
            print(f"Round {round + 1}:")
            self.play_round()
        print("\nGame over!")
        print(f"\nFinal scores are Player 1: {self.p1_score}")
        print(f"Player 2: {self.p2_score}")
        print(f"and {self.ties} tie(s)!")


if __name__ == '__main__':

    # Play against Player that always plays 'rock'
    print("\n\nPlaying against 'rock' Player\n\n")
    game = Game(Player(), RandomPlayer())
    game.play_game()

    # Play RandomPlayer vs HumanPlayer
    print("\n\nPlaying against Random Player\n\n")
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()

    # Play ReflectPlayer vs HumanPlayer
    print("\n\nPlaying against Reflect Player\n\n")
    game = Game(ReflectPlayer(), HumanPlayer())
    game.play_game()

    # Play CyclePlayer vs HumanPlayer
    print("\n\nPlaying against Cycle Player\n\n")
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
