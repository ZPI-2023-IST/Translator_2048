from abc import ABC, abstractmethod


class AbstractTranslator(ABC):
    def __init__(self, game=None):
        self.game = game

    @abstractmethod
    def make_move(self, move):
        """
        Make a move_vector in a game
        """
        pass

    @abstractmethod
    def get_moves(self):
        """
        Get list of possible moves from the game and convert them to model input
        """
        pass

    @abstractmethod
    def get_board(self):
        """
        Get board from the game and convert it to model input
        """
        pass

    @abstractmethod
    def get_state(self):
        """
        Get from the game its current status
        """
        pass

    @abstractmethod
    def start_game(self):
        """
        Start game
        """
        pass

    @abstractmethod
    def get_reward(self):
        """
        Get reward for the given board
        """
        pass

    @abstractmethod
    def get_config_model(self):
        """
        Get params that can be used later to construct a model
        """
        pass