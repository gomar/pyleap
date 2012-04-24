import numpy as np


class HbComputation():
    """
    Defines an Almost-Periodic Computation. The IDFT and DFT
    Almost-Periodic Matrix can be computed
    """

    def __init__(self, frequencies, timelevels=None):
        self.set_frequencies(frequencies)
        if timelevels == None:
            N = len(self.frequencies)
            self.set_timelevels(timelevels=\
                           self.get_evenly_spaced(sampling=2 * N + 1))
        else:
            self.set_timelevels(timelevels)
    
    def set_timelevels(self, timelevels):
        self.timelevels = np.array(timelevels, dtype=float)
    
    def set_frequencies(self, frequencies):
        self.frequencies = np.array(frequencies, dtype=float)
    
    def get_evenly_spaced(self, sampling=None, base_frequency=None):
        """
        Set the timelevels vector as evenly spaced
        with a given sampling. If None is given,
        the sampling is 2 * len(frequencies) + 1
        """
        if not sampling:
            sampling = 2 * len(self.frequencies) + 1

        if not base_frequency:
            base_frequency = np.min(np.absolute(self.frequencies))

        # casting sampling to a float so that int division does not occur
        sampling = sampling + 0.
        return np.arange(sampling) / (base_frequency * sampling)

    def ap_idft_matrix(self, frequencies=None, timelevels=None):
        """
        Compute the Almost-Periodic IDFT matrix
        """
        # if no frequencies are given, then it is the one of
        # the HbComputation
        if frequencies == None:
            frequencies = self.frequencies
        else:
            frequencies = np.array(frequencies, dtype=float)
        # same for the timelevels
        if timelevels == None:
            timelevels = self.timelevels
        else:
            timelevels = np.array(timelevels, dtype=float)

        # reshaping the timelevels vector so that a matrix
        # product can be done with the frequencies
        timelevels = timelevels.reshape((timelevels.shape[0], 1))
        # building the symmetric vector of frequencies
        frequencies = np.insert(frequencies, 0, 0)
        frequencies = np.append(-frequencies[:0:-1], frequencies)
        frequencies = frequencies.reshape((1, frequencies.shape[0]))
        return np.exp(2 * 1j * np.pi * np.dot(timelevels, frequencies))

    def ap_dft_matrix(self, frequencies=None, timelevels=None):
        """
        Compute the Almost-Periodic DFT matrix
        """
        return np.linalg.pinv(self.ap_idft_matrix(frequencies=frequencies,
                                                  timelevels=timelevels))

    def conditionning(self):
        """
        Returns the condition number of the almost periodic IDFT matrix 
        """
        return np.linalg.cond(self.ap_idft_matrix())
