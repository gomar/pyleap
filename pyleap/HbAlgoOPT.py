"""
Implementation of a gradient-based algorithm over the
condition number
"""

from pyleap.HbAlgoInterface import HbAlgoInterface
from pyleap.HbComputation import HbComputation
from scipy.optimize import fmin_l_bfgs_b
import numpy as np


class HbAlgoOPT(HbAlgoInterface):

    def __init__(self, frequencies, target=0.):
        self.frequencies = np.array(frequencies, dtype=float)
        self.target = float(target)

    def _conditionning(self, timelevels):
        hb_computation = HbComputation(frequencies=self.frequencies,
                                       timelevels=timelevels)
        return abs(hb_computation.conditionning() - self.target)

    def optimize_timelevels(self):
        # sampling the minimum frequency to get fractions
        # of the greatest period
        freq_min = np.min(np.absolute(self.frequencies))
        number_of_samples = 1000
        freq_sample = 1. / (np.linspace(0., freq_min,
                                        number_of_samples) + freq_min / 500.)
        # the freq_sample vector is reshaped so that a matrix product
        # can be done to efficiently compute all the time levels
        # that will be used as possibly starting point
        freq_sample = freq_sample.reshape((1, freq_sample.shape[0]))

        # number of samples used for the timelevels is
        # 2N+1 where N is the number of frequencies
        N = len(self.frequencies)
        timelevels = np.linspace(0., 1., 2 * N + 1.)
        # timelevels vector is also reshape so that the matrix
        # product can be done
        timelevels = timelevels.reshape((timelevels.shape[0], 1))

        # the timelevels vector is now a matrix that
        # contains initial sampling of evenly spaced time levels
        # taken in fractions of the greatest period
        timelevels = np.dot(timelevels, freq_sample)

        # initializing the result matrix with stupid values
        result = np.empty(timelevels.shape[1])

        # computing the condition number of each evenly spaced
        # timelevels and choosing the best one as an initial value
        # for the L-BFGS-B algorithm
        for tlv in range(timelevels.shape[1]):
            result[tlv] = self._conditionning(timelevels=timelevels[:, tlv])
        # indice of the time levels vector that gave the minimum
        # condition number
        min_conditionning = np.argmin(result)

        # the L-BFGS-B algortihm can have bounds that he can not cross.
        # As the first time levels is always chosen to be 0.
        # the bounds are set as follows
        bounds = [(None, None) for i in range(2 * N + 1)]
        bounds[0] = (0., 0.)
        return fmin_l_bfgs_b(func=self._conditionning,
                             x0=timelevels[:, min_conditionning],
                             bounds=bounds,
                             approx_grad=True)[0]
