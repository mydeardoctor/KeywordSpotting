import collections

import numpy as np


class Preprocessor:
    @staticmethod
    def preprocess(one_second_buffer: collections.deque) -> np.ndarray:
        bytes_data = bytes(one_second_buffer)
        audio: np.ndarray = np.frombuffer(buffer=bytes_data,
                                          dtype=np.int16)
        audio = np.expand_dims(a=audio,
                               axis=0)       
        return audio