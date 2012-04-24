#
#  bench_algo.py
#  PyLeap
#
#  Created by Adrien Gomar on 2012-04-24.
#  Copyright 2012 CERFACS. All rights reserved.
#

"""
Script to estimate the performance of sampling
algorithms for almost-periodic computations.
"""

import sys
# dirty way to add module to pythonpath
sys.path.append('../..')

from pyleap import HbComputation, HbAlgoAPFT, HbAlgoOPT, HbAlgoEQUI
import numpy as np


def conditionning_algo(f, f1, algo_choice):
    """
    Function that computes the best condition number
    found by the given algorithm.
    """
    frequencies = [f, f1]
    frequencies.sort()

    # initializing the HbComputation object with the given frequencies
    hb_computation = HbComputation(frequencies=frequencies)

    # initializing the chosen algorithm
    if algo_choice == 'OPT':
        hb_algo = HbAlgoOPT(frequencies=frequencies)
    if algo_choice == 'APFT':
        hb_algo = HbAlgoAPFT(frequencies=frequencies)
    elif algo_choice == 'EQUI_2N_1':
        hb_algo = HbAlgoEQUI(frequencies=frequencies,
                          sampling=2 * len(frequencies) + 1)
    elif algo_choice == 'EQUI_3N_1':
        hb_algo = HbAlgoEQUI(frequencies=frequencies,
                          sampling=3 * len(frequencies) + 1)
    elif algo_choice == 'EQUI_20N_1':
        hb_algo = HbAlgoEQUI(frequencies=frequencies,
                          sampling=20 * len(frequencies) + 1)

    # setting the optimized time levels to compute the
    # almost periodic DFT matrix condition number
    hb_computation.set_timelevels(hb_algo.optimize_timelevels())
    return hb_computation.conditionning()


def main(algo_choice, sampling, f1):
    """
    Main function: computes the delta_f_star, and run all
    the call to the conditionning function
    """
    # computing delta_f_star and the corresponding f vector
    delta_f_star = np.linspace(0.001, 1.999, num=sampling)
    f = f1 * (2 - delta_f_star) / (delta_f_star + 2)

    # intializaing the results
    result = np.empty((sampling, 2))
    result[:, 0] = delta_f_star

    # vectorializing the function to run faster
    # (C loops instead of python ones)
    vfunc = np.vectorize(conditionning_algo)
    result[:, 1] = vfunc(f, f1, algo_choice)

    # printing global infos that are not saved to a file
    print 'ALGO: %s' % algo_choice
    print ('mean', np.mean(result[:, 1]),
           'min', np.min(result[:, 1]),
           'max', np.max(result[:, 1]))
    print ''

    # saving the result (delta_f_star, conditionning) to a file
    np.savetxt(fname='BENCH_ALGO_%s.dat' % algo_choice, X=result)

if __name__ == '__main__':

    # base frequency to compute the delta_f_star
    # delta_f_star is defined as
    # delta_f_star = 2*(f1-f)/(f1+f)
    F1 = 3.
    # number of samples for delta_f_star discretization
    SAMPLING = 1000

    # launching all the algorithms
    for algo in ['EQUI_2N_1', 'EQUI_3N_1',
                        'EQUI_20N_1', 'OPT', 'APFT']:
        main(algo_choice=algo,
             sampling=SAMPLING,
             f1=F1)
