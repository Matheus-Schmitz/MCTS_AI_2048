import random

from Board import Board
from MonteCarloTreeSearch import MonteCarloTreeSearch

NUMBER_OF_ITERATIONS = 1


def get_random_direction():
    return directions[random.randint(0, len(directions) - 1)]


directions = ['up', 'down', 'right', 'left']

for i in range(0, NUMBER_OF_ITERATIONS):
    board = Board()
    while True:
        result_scores = list()
        for direction in directions:
            next_board_state = board.simulate_next_move(direction)
            monte_carlo_search = MonteCarloTreeSearch()
            result_score = monte_carlo_search.pure_monte_carlo_search(next_board_state, board.score)
            result_scores.append(result_score)
        direction_decision = directions[result_scores.index(max(result_scores))]
        board.move_board(direction_decision)
        board.add_random_tile()
        if board.is_game_over() is True:
            print('game over, score:' + str(board.score))
            board_states, score = board.get_board_states_and_score()
            board.print_board()
            break
