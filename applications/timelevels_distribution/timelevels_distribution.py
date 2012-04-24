# 
#  timelevels_distribution.py
#  PyLeap
#  
#  Created by Adrien Gomar on 2012-04-24.
#  Copyright 2012 CERFACS. All rights reserved.
# 

"""
Script to generate the evenly spaced time levels
and the distribution of an optimized set of 
non evenly spaced timelevels in each frequency
period
"""

import sys
# dirty way to add module to pythonpath
sys.path.append('../..')

import pyleap
import numpy as np

FREQ = [3., 17.]

HB_COMPUTATION = pyleap.HbComputation(frequencies=FREQ)

DISTRIBUTION_F1 = np.empty((2 * len(FREQ) + 1, 4))
DISTRIBUTION_F2 = np.empty((2 * len(FREQ) + 1, 4))

# non-dimensional evenly spaced timelevels serving as
# references for the plot of the distribution
DISTRIBUTION_F1[:, 0] = np.arange(0., 2 * len(FREQ) + 1) / (2 * len(FREQ) + 1)
DISTRIBUTION_F2[:, 0] = DISTRIBUTION_F1[:, 0]

# evenly spaced with sampling 2N+1, EQUI
ALGO = pyleap.HbAlgoEQUI(frequencies=FREQ, sampling=2 * len(FREQ) + 1)
HB_COMPUTATION.set_timelevels(ALGO.optimize_timelevels())
DISTRIBUTION_F1[:, 1] = np.sort((HB_COMPUTATION.timelevels % (1. / FREQ[0])) * FREQ[0])
DISTRIBUTION_F2[:, 1] = np.sort((HB_COMPUTATION.timelevels % (1. / FREQ[1])) * FREQ[1])
print 'Algo EQUI, cond:', HB_COMPUTATION.conditionning()

# using APFT algorithm
ALGO = pyleap.HbAlgoAPFT(frequencies=FREQ)
HB_COMPUTATION.set_timelevels(ALGO.optimize_timelevels())
DISTRIBUTION_F1[:, 2] = np.sort((HB_COMPUTATION.timelevels % (1. / FREQ[0])) * FREQ[0])
DISTRIBUTION_F2[:, 2] = np.sort((HB_COMPUTATION.timelevels % (1. / FREQ[1])) * FREQ[1])
print 'Algo APFT, cond:', HB_COMPUTATION.conditionning()

# using OPT algorithm
ALGO = pyleap.HbAlgoOPT(frequencies=FREQ)
HB_COMPUTATION.set_timelevels(ALGO.optimize_timelevels())
DISTRIBUTION_F1[:, 3] = np.sort((HB_COMPUTATION.timelevels % (1. / FREQ[0])) * FREQ[0])
DISTRIBUTION_F2[:, 3] = np.sort((HB_COMPUTATION.timelevels % (1. / FREQ[1])) * FREQ[1])
print 'Algo OPT, cond:', HB_COMPUTATION.conditionning()

np.savetxt('TIMELEVELS_DISTRIBUTION_F1.dat', DISTRIBUTION_F1)
np.savetxt('TIMELEVELS_DISTRIBUTION_F2.dat', DISTRIBUTION_F2)
