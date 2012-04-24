from pyleap import HbComputation, HbAlgoAPFT, HbAlgoOPT, HbAlgoEQUI
import numpy as np


def main(f, f1, algo_choice, sampling=None):
    # initializing the HbComputation object with the given frequencies
    FREQ = [f1, f]
    FREQ.sort()
    hb_computation = HbComputation(frequencies=FREQ)
    
    # initializing the chosen algorithm
    if algo_choice == 'OPT':
        ALGO = HbAlgoOPT(frequencies=FREQ)
    if algo_choice == 'APFT':
        ALGO = HbAlgoAPFT(frequencies=FREQ)
    elif algo_choice == 'EQUI_2N_1':
        ALGO = HbAlgoEQUI(frequencies=FREQ, sampling=2 * len(FREQ) + 1)
    elif algo_choice == 'EQUI_3N_1':
        ALGO = HbAlgoEQUI(frequencies=FREQ, sampling=3 * len(FREQ) + 1)
    elif algo_choice == 'EQUI_20N_1':
        ALGO = HbAlgoEQUI(frequencies=FREQ, sampling=20 * len(FREQ) + 1)
    
    # setting the optimized time levels to compute the DFT condition number
    hb_computation.set_timelevels(ALGO.optimize_timelevels())
    return hb_computation.conditionning()

if __name__ == '__main__':
    
    
    def launch(ALGO_CHOICE):
        # base frequency to compute the delta_f_star
        f1 = 3.
        # number of samples for delta_f_star discretization
        SAMPLING = 1000
        # computing delta_f_star and the corresponding f vector
        delta_f_star = np.linspace(0.001, 1.999, num=SAMPLING)
        f2 = f1 * (2 - delta_f_star) / (delta_f_star + 2)

        # intializaing the results
        RESU = np.empty((1000, 2))        
        RESU[:, 0] = delta_f_star
        
        # vectorializing the function to run faster (C loops instead of python ones)
        vfunc = np.vectorize(main)
        RESU[:, 1] =  vfunc(f2, f1, ALGO_CHOICE)
        
        # printing global infos that are not saved to a file
        print 'ALGO: %s' % ALGO_CHOICE
        print 'mean', np.mean(RESU[:, 1]), 'min', np.min(RESU[:, 1]), 'max', np.max(RESU[:, 1]) 
        print ''
        
        # saving the result (delta_f_star, conditionning) to a file
        np.savetxt(fname='BENCH_ALGO_%s.dat' % ALGO_CHOICE, X=RESU)
        
    # launching all the algorithms   
    launch('EQUI_2N_1')
    launch('EQUI_3N_1')
    launch('EQUI_20N_1')
    launch('OPT')
    launch('APFT')