"""
Script to generate the equi timelevels
and the distribution of an optimized set of 
non evenly spaced timelevels in each frequency
period

uses pyleap v0.1
"""

import pyleap
import numpy as np
from copy import deepcopy

FREQ = [3., 17.]

hb_computation = pyleap.HbComputation(frequencies=FREQ)

distribution_f1 = np.empty((2 * len(FREQ) + 1, 4))
distribution_f2 = np.empty((2 * len(FREQ) + 1, 4))

# non-dimensional evenly spaced timelevels serving as
# references for the plot of the distribution
distribution_f1[:, 0] = np.arange(0., 2 * len(FREQ) + 1) / (2 * len(FREQ) + 1)
distribution_f2[:, 0] = distribution_f1[:, 0]

# evenly spaced with sampling 2N+1, EQUI
ALGO = pyleap.HbAlgoEQUI(frequencies=FREQ, sampling=2 * len(FREQ) + 1)
hb_computation.set_timelevels(ALGO.optimize_timelevels())
distribution_f1[:, 1] = np.sort((hb_computation.timelevels % (1. / FREQ[0])) * FREQ[0])
distribution_f2[:, 1] = np.sort((hb_computation.timelevels % (1. / FREQ[1])) * FREQ[1])
print 'Algo EQUI, cond:', hb_computation.conditionning()

# using APFT algorithm
ALGO = pyleap.HbAlgoAPFT(frequencies=FREQ)
hb_computation.set_timelevels(ALGO.optimize_timelevels())
distribution_f1[:, 2] = np.sort((hb_computation.timelevels % (1. / FREQ[0])) * FREQ[0])
distribution_f2[:, 2] = np.sort((hb_computation.timelevels % (1. / FREQ[1])) * FREQ[1])
print 'Algo APFT, cond:', hb_computation.conditionning()

# using OPT algorithm
ALGO = pyleap.HbAlgoOPT(frequencies=FREQ)
hb_computation.set_timelevels(ALGO.optimize_timelevels())
distribution_f1[:, 3] = np.sort((hb_computation.timelevels % (1. / FREQ[0])) * FREQ[0])
distribution_f2[:, 3] = np.sort((hb_computation.timelevels % (1. / FREQ[1])) * FREQ[1])
print 'Algo OPT, cond:', hb_computation.conditionning()

np.savetxt('TIMELEVELS_DISTRIBUTION_F1.dat', distribution_f1)
np.savetxt('TIMELEVELS_DISTRIBUTION_F2.dat', distribution_f2)
