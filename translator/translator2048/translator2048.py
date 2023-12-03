import math

from .constants import *
from ..abstract_translator.AbstractTranslator import AbstractTranslator


class Translator2048(AbstractTranslator):

    def __init__(self, game=None):
        super().__init__(game)
        self.move_indexes = list(MOVES)

    def make_move(self, move_index):
        move_vector = self.move_indexes[move_index].value[1]
        matching_move = next(move for move in MOVES if move.value[1] == move_vector)
        move = matching_move.value[0]
        self.game.make_move((move,))
        return True

    def get_moves(self):
        all_moves = self.game.get_moves()
        moves_indexes = [self.move_indexes.index(get_enum_member(move)) for move in all_moves]
        return moves_indexes

    def get_board(self):
        board = self.game.get_board()
        board_one_hot_values = [FIELDS_VALUES[field.value] for row in board for field in row]
        return board_one_hot_values

    def get_state(self):
        return self.game.get_state()

    def start_game(self):
        self.game.start_game()

    def get_reward(self):
        state = self.game.get_state()
        if state.value == State.WON.value:
            return 10
        elif state.value == State.LOST.value:
            return -10
        else:
            # Modify merge_reward and empty_penalty to handle None values
            merge_reward = sum([tile.value for row in self.game.get_board() for tile in row if tile.value is not None])
            empty_penalty = -0.1 * len(
                [tile.value for row in self.game.get_board() for tile in row if tile.value is None])

            monotonic_reward = self.__calculate_monotonic_reward()  # Reward for board monotonicity
            smoothness_reward = self.__calculate_smoothness_reward()  # Reward for smoothness

            total_reward = merge_reward + empty_penalty + monotonic_reward + smoothness_reward
            normalized_reward = math.log(total_reward + 1) / 2  # Logarithmic normalization
            scaled_reward = min(10, max(0, normalized_reward))  # Scale to be between 0 and 10

            return scaled_reward

    def get_config_model(self):
        pass

    def __calculate_smoothness_reward(self):
        smoothness_reward = 0
        board = self.game.get_board()
        for row in board:
            for i in range(1, len(row)):
                if row[i].value is not None and row[i - 1].value is not None:
                    smoothness_reward -= abs(row[i].value - row[i - 1].value)

        for col in zip(*board):
            for i in range(1, len(col)):
                if col[i].value is not None and col[i - 1].value is not None:
                    smoothness_reward -= abs(col[i].value - col[i - 1].value)

        return smoothness_reward

    def __calculate_monotonic_reward(self):
        monotonic_reward = 0
        board = self.game.get_board()

        for row in board:
            monotonic_reward += sum([abs(row[i].value or 0 - row[i - 1].value) for i in range(1, len(row)) if
                                     None not in (row[i].value, row[i - 1].value)])

        for col in zip(*board):
            monotonic_reward += sum([abs((col[i].value or 0) - (col[i - 1].value or 0)) for i in range(1, len(col)) if
                                     None not in (col[i].value, col[i - 1].value)])

        return monotonic_reward
