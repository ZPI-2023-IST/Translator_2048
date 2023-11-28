from ..abstract_translator.AbstractTranslator import AbstractTranslator
from .constants import *
import math

class Translator2048(AbstractTranslator):

    def __init__(self, game=None):
        super().__init__(game)

    def make_move(self, move_vector):
        matching_move = next(move for move in MOVES if move.value[1] == move_vector)
        move = matching_move.value[0]
        self.game.make_move((move,))
        return True

    def get_moves(self):
        all_moves = self.game.get_moves()
        moves_one_hot = [move.value[1] for move in MOVES if move.value[0] in all_moves]
        return moves_one_hot

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
            return 5
        elif state.value == State.LOST.value:
            return -5
        else:
            num_moves = len(self.game.get_moves())
            normalized_reward = math.log(num_moves + 1) / 2  # Logarithmic normalization
            scaled_reward = min(5, max(0, normalized_reward))  # Scale to be between 0 and 5
            return scaled_reward

    def get_config_model(self):
        pass
