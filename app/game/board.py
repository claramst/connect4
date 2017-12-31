import numpy as np
import pandas as pd

N = 6


class Board:

    def __init__(self):
        self.board = np.zeros((N, N), dtype=np.int)

    def fill_example(self):
        self.board[3, 0] = 1
        self.board[3, 1] = 2
        self.board[3, 2] = 1
        self.board[3, 3] = 2
        return

    def as_pandas(self):
        return pd.DataFrame(self.board)