import random
import sys
from copy import copy, deepcopy


class Board:
    def __init__(self, board=None, score=None):
        self.previous_board_state = None
        self.size = 4
        self.start_tiles = 2
        if not score:
            self.score = score

        self.score = 0
        self.board_tracker = list()
        if board is None:
            self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
            for i in range(self.start_tiles):
                self.add_random_tile()
        else:
            self.board = board
            # self._track_board_state()

    def add_random_tile(self):
        if self.is_add_random_tile():
            value_to_add = self.generate_random_value()
            available_cells = self.get_available_cells()
            rand_index = random.randint(0, len(available_cells) - 1)
            chosen_cell = available_cells[rand_index]
            self.board[chosen_cell[0]][chosen_cell[1]] = value_to_add

    def is_add_random_tile(self):
        return self.is_cells_available() and self.is_previous_state_changed()

    def is_previous_state_changed(self):
        if self.previous_board_state is None:
            return True

        if self.previous_board_state == self.board:
            return False
        else:
            return True

    def is_cells_available(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return True
        return False

    def get_available_cells(self):
        width = len(self.board)
        found = []
        position = 0
        for row in self.board:
            for value in row:
                if value == 0:
                    found.append((position // width, position % width))
                position += 1
        return found

    @staticmethod
    def generate_random_value():
        rand_int = random.randint(1, 10)
        value_to_add = 2
        if rand_int > 9:
            value_to_add = 4
        return value_to_add

    def move_board(self, direction):
        self.previous_board_state = deepcopy(self.board)
        merged_lists = list()
        lists_to_merge = self._get_lists_to_merge(direction)
        for i in range(0, self.size):
            if direction is 'down' or direction is 'right':
                merged_lists.append(list(reversed(self._merge(list(reversed(lists_to_merge[i]))))))
            else:
                merged_lists.append(self._merge(lists_to_merge[i]))

        self.board = self._reassemble_vertical_lists(merged_lists, direction)
        print("Current Score: " + str(self.score) + " Max Tile: " + str(self.get_max_tile()))

    def move_board_random(self):
        directions = ['up', 'down', 'right', 'left']
        direction = directions[random.randint(0, len(directions) - 1)]
        merged_lists = list()
        lists_to_merge = self._get_lists_to_merge(direction)
        for i in range(0, self.size):
            if direction is 'down' or direction is 'right':
                merged_lists.append(list(reversed(self._merge(lists_to_merge[i]))))
            else:
                merged_lists.append(self._merge(lists_to_merge[i]))

        self.board = self._reassemble_vertical_lists(merged_lists, direction)
        # self._track_board_state()

    def _reassemble_vertical_lists(self, merged_lists, direction):
        if direction is 'down' or direction is 'up':
            tuples = copy(merged_lists)
            for i in range(0, self.size):
                merged_lists[i] = list(tuples[i])
        return merged_lists

    def _merge(self, list_to_merge):
        non_zeros_removed = []
        result = []
        merged = False
        for value in list_to_merge:
            if value != 0:
                non_zeros_removed.append(value)

        while len(non_zeros_removed) != len(list_to_merge):
            non_zeros_removed.append(0)

        # Double sequential tiles if same value
        for number in range(0, len(non_zeros_removed) - 1):
            first_pair = non_zeros_removed[number]
            second_pair = non_zeros_removed[number+1]

            if first_pair == second_pair and first_pair != 0 and second_pair != 0 and merged is False:
                result.append(first_pair * 2)
                merged = True
                self.score += first_pair * 2
            elif first_pair != second_pair and merged is False:
                result.append(first_pair)
            elif merged:
                merged = False

        if non_zeros_removed[-1] != 0 and merged is False:
            result.append(non_zeros_removed[-1])

        while len(result) != len(non_zeros_removed):
            result.append(0)

        return result

    def _get_lists_to_merge(self, direction):
        if direction is "up" or direction is "down":
            lists_to_merge = self._get_columns()
        else:
            lists_to_merge = self._get_rows()
        return lists_to_merge

    def _get_rows(self):
        rows = list()
        for row in self.board:
            rows.append(row)
        return rows

    def _get_columns(self):
        columns = list()
        for i in range(self.size):
            column = list()
            for row in self.board:
                column.append(row[i])
            columns.append(column)
        return columns

    def print_board(self):
        for row in self.board:
            for value in row:
                sys.stdout.write('|' + str(value) + '|')
            sys.stdout.write("\n")
        sys.stdout.write("----\n")

    def _track_board_state(self):
        self.board_tracker.append(self.board)

    def get_board_states_and_score(self):
        return self.board_tracker, self.score

    def simulate_next_move(self, direction):
        """Simulates next move and returns the resulting board"""
        merged_lists = list()
        lists_to_merge = self._get_lists_to_merge(direction)
        for i in range(0, self.size):
            if direction is 'down' or direction is 'right':
                merged_lists.append(list(reversed(self._merge(list(reversed(lists_to_merge[i]))))))
            else:
                merged_lists.append(self._merge(lists_to_merge[i]))

        return self._reassemble_vertical_lists(merged_lists, direction)

    def is_match_available(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                current_cell = self.board[i][j]
                if i != 0:
                    up_cell = self.board[i - 1][j]
                    if current_cell == up_cell:
                        return True
                if i != len(self.board[i]) - 1:
                    down_cell = self.board[i + 1][j]
                    if current_cell == down_cell:
                        return True
                if j != 0:
                    left_cell = self.board[i][j - 1]
                    if current_cell == left_cell:
                        return True
                if j != len(self.board) - 1:
                    right_cell = self.board[i][j + 1]
                    if current_cell == right_cell:
                        return True
        return False

    def get_max_tile(self):
        max_values = list()
        for x in range(0, len(self.board)):
            max_values.append(max(self.board[x]))
        return max(max_values)

    def is_game_over(self):
        if self.is_cells_available() or self.is_match_available():
            return False
        return True
