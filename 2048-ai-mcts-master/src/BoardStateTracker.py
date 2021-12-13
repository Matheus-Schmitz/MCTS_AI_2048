import uuid
import pickle


class BoardStateTracker:
    def __init__(self):
        self.aggregate_count = 0
        self.aggregate_number = 10000
        self.output_path = 'BoardStates\\'
        self.board_state_list = list()

    def save_board_states(self, board_states, score):
        self._save_board_states(board_states, score)
        return

    def _save_board_states(self, board_states, score):
        board_dict = {'board_states': board_states, 'end_score': score}
        self.board_state_list.append(board_dict)
        self.aggregate_count += 1
        if self.aggregate_count == self.aggregate_number:
            self._serialize_board_states()

    def _serialize_board_states(self):
        uuid_token = uuid.uuid4()
        pickle.dump(self.board_state_list, open(self.output_path + str(uuid_token), 'wb'))
        self.board_state_list = list()
        self.aggregate_count = 0
        print('board state serialization complete')
