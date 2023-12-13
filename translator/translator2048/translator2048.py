import math

from .constants import *
from ..abstract_translator.AbstractTranslator import AbstractTranslator


class Translator2048(AbstractTranslator):

    def __init__(self, game=None):
        super().__init__(game)
        self.move_indexes = list(MOVES)
        self.prev_board_empty_cells = None

    def make_move(self, move_index):
        move = MOVES[move_index]
        self.game.make_move((move,))
        return True

    def get_moves(self):
        all_moves = self.game.get_moves()
        moves_indexes = [MOVES.index(move) for move in all_moves]
        return moves_indexes

    def get_board(self):
        board = self.game.get_board()
        board_one_hot_values = [FIELDS_VALUES[field.value] for row in board for field in row]
        return board_one_hot_values

    def get_state(self):
        return self.game.get_state()

    def start_game(self):
        self.prev_board_empty_cells = None
        self.game.start_game()

    def get_reward(self):
        state = self.game.get_state()
        if state.value == State.WON.value:
            return 100
        elif state.value == State.LOST.value:
            return -100
        else:
            reward = self.__count_monotonicity_reward()
            normalized_reward = math.log(reward + 1)/2  # Logarithmic normalization
            scaled_reward = min(10, max(0, normalized_reward))
            return scaled_reward

    def __count_monotonicity_reward(self):
        best = -1

        board = [
            [x.value if x.value is not None else 0 for x in row]
            for row in self.game.get_board()
        ]

        for i in range(4):
            current = 0

            for row in range(4):
                for col in range(3):
                    if board[row][col] >= board[row][col + 1]:
                        current += 1

            for col in range(4):
                for row in range(3):
                    if board[row][col] >= board[row + 1][col]:
                        current += 1

            if current > best:
                best = current

            # Rotate the board 90 degrees clockwise
            board = self.__rotate_board_clockwise(board)

        return best

    def __rotate_board_clockwise(self,board):
        return [[board[3 - row][col] for row in range(4)] for col in range(4)]


    def get_config_model(self):
        pass


