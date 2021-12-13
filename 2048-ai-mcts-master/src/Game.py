from Board import Board


class Game:
    def __init__(self):
        pass

    def play_random_with_state(self, board_state, score):
        """Start playing from the given board state and return score"""
        board = Board(board_state, score)

        while True:
            board.move_board_random()
            board.add_random_tile()
            if board.is_game_over() is True:
                board_states, score = board.get_board_states_and_score()
                return score
