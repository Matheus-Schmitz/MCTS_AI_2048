from Game import Game

MONTE_CARLO_ITERATIONS = 25


class MonteCarloTreeSearch:
    def __init__(self):
        pass

    def pure_monte_carlo_search(self, board_state, score):
        """play with random moves given a board state and return average score"""
        scores = list()
        for i in range(0, MONTE_CARLO_ITERATIONS):
            game = Game()
            score = game.play_random_with_state(board_state, score)
            scores.append(score)

        return sum(scores) / len(scores)
