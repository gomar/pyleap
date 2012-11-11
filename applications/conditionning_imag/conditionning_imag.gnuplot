# 
#  conditionning_imag.gnuplot
#  PyLeap
#  
#  Created by Adrien Gomar on 2012-04-24.
#  Copyright 2012 CERFACS. All rights reserved.
# 

# global style definition
set style line 1 linetype -1 linewidth 1
set style line 2 linetype 3 linewidth 2
set style line 3 linetype -1 linewidth 2

# set labels
set xlabel '$\kappa(A)$'
set ylabel '$\frac{\|Im(D_t)\|_F}{\|Re(D_t)\|_F}$'
set format y "$10^{%T}$"

# global parameters
set terminal epslatex standalone
set xrange [1:10000000]
set yrange [0.0000000000000001:0.0000001]
set logscale x
set logscale y

# legend definition
# if you have gnuplot >= 4.6 put opaque filter to the key
unset key

#@@@@@@@@@@@@@@@@@@@@@@@@@@@
# figure
#@@@@@@@@@@@@@@@@@@@@@@@@@@@

# figure for the proposed algorithms
set output 'CONDITIONNING_IMAG.tex'
plot 'CONDITIONNING_IMAG.dat' w l ls 1 title 'test
