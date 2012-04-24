from pyleap.ApAlgoInterface import ApAlgoInterface 
import numpy as np


class ApAlgoEQUI(ApAlgoInterface):

    def __init__(self, frequencies, sampling=None):
        self.frequencies = np.array(frequencies, dtype=float)
        if sampling == None:
            sampling = 2 * len(self.frequencies) + 1
        self.sampling = float(sampling)
    
    def optimize_timelevels(self):
        freq_min = np.min(np.absolute(self.frequencies))
        return np.arange(0., self.sampling) / (freq_min * self.sampling)
