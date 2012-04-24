# 
#  HbAlgoAPFT.py
#  PyLeap
#  
#  Created by Adrien Gomar on 2012-04-24.
#  Copyright 2012 CERFACS. All rights reserved.
# 

from pyleap.HbAlgoInterface import HbAlgoInterface 
from scipy.optimize import fminbound
from pyleap.HbComputation import HbComputation
import numpy as np


class HbAlgoAPFT:
    """
    Implementation of the APFT algorithm defined in
    Kundert et al. "Applying Harmonic Balance to Almost-Periodic Circuits"
    """
    
    def __init__(self, frequencies):
        self.frequencies = np.array(frequencies, dtype=float)

    def _conditionning(self, timelevels):
        ap_computation = HbComputation(frequencies=self.frequencies,
                                       timelevels=timelevels)
        return ap_computation.conditionning()

    def optimize_timelevels(self):
        
        def apft_conditionning(over_sampling):
            return self._conditionning(timelevels=self.apft(over_sampling))
            
        N = len(self.frequencies)
        # the oversampling corresponding to the optimized timelevels is:
        over_sampling_opt = fminbound(func=apft_conditionning,
                                      x1=2 * N + 2, 
                                      x2=100 * N)

        return self.apft(over_sampling_opt)

        
    def apft(self, over_sampling):

        N = len(self.frequencies)

        # choosing the samllest frequence on which
        # the timelevels will be discretized
        freq_min = np.min(np.absolute(self.frequencies))
        timelevels = 6 * np.arange(0, 1., 1. / float(over_sampling)) / freq_min
        ap_computation = HbComputation(frequencies=self.frequencies,
                                       timelevels=timelevels)
        
        # computing the corresponding hbt_matrix
        ap_idft_matrix = ap_computation.ap_idft_matrix()
        
        for line in range(0, 2 * N + 1):
            # gramm-schmidt kinf of orthonormalization
            ap_idft_matrix[line + 1:, :] -= np.sum(np.dot(ap_idft_matrix[line + 1:, :],
                                                   np.diag(ap_idft_matrix[line, :])),
                                               axis=0) / \
                                        np.sum(ap_idft_matrix[line, :] ** 2) * \
                                        ap_idft_matrix[line, :]

            # choossing the vector that was most othogonal to
            # the one of line
            k = np.argmax([np.linalg.norm(ap_idft_matrix[line_ind],
                                          np.inf)
                           for line_ind in range(line, len(timelevels))])

            # swapping vectors
            ap_idft_matrix[[line, k], :] = ap_idft_matrix[[k, line], :]
            timelevels[[0, k]] = timelevels[[k, 0]]

        del ap_idft_matrix

        timelevels = timelevels[:2 * N + 1]
        timelevels.sort(0)
        return timelevels
