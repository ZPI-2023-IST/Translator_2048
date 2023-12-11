import math

from .constants import *
from ..abstract_translator.AbstractTranslator import AbstractTranslator


class Translator2048(AbstractTranslator):

    def __init__(self, game=None):
        super().__init__(game)
        self.move_indexes = list(MOVES)
        self.prev_board_empty_cells = None

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
            current_board_empty_cells = len([node.value for row in self.game.get_board() for node in row if node.value is None] )
            if self.prev_board_empty_cells is None:
                self.prev_board_empty_cells = current_board_empty_cells
                return 0

            # Calculate the change in the number of empty cells
            empty_cells_change = current_board_empty_cells - self.prev_board_empty_cells

            # Update the previous empty cells count
            self.prev_board_empty_cells = current_board_empty_cells

            # Calculate the reward based on the change in empty cells
            reward = empty_cells_change

            return reward

    def get_config_model(self):
        pass


