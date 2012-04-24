#@@@@@@@@@@@@@@@@@@@@@@@@@@@
# paper plot, initialization
#@@@@@@@@@@@@@@@@@@@@@@@@@@@

# global style definition
set style line 1 linetype -1 linewidth 1
set style line 2 linetype 3 linewidth 2
set style line 3 linetype -1 linewidth 2

# set labels
set xlabel '$\delta_f^* = 2 \cdot \displaystyle\frac{f_1 - f}{f_1 + f}$' offset 0, -0.5
set ylabel '$\kappa(A)$'

# global parameters
set terminal epslatex standalone
set xrange [0.001:1.999]
set yrange [1:100]
set xtics 0, 0.5, 2
set logscale y

# legend definition
# if you have gnuplot >= 4.6 put opaque filter to the key
set key reverse Left box spacing 1.5 left

#@@@@@@@@@@@@@@@@@@@@@@@@@@@
# figure
#@@@@@@@@@@@@@@@@@@@@@@@@@@@

# figure for the proposed algorithms
set output 'BENCH_ALGO_PA.tex'
plot 'BENCH_ALGO_APFT.dat' w l ls 2 title 'APFT ', \
'BENCH_ALGO_OPT.dat' w l ls 3 title 'OPT', \
'BENCH_ALGO_EQUI_2N_1.dat' w l ls 1 title 'EQUI $2N+1$  '

# figure for the EQUI algorithms
set output 'BENCH_ALGO_EQUI.tex'
plot 'BENCH_ALGO_EQUI_2N_1.dat' w l ls 1 title '$2N+1$   ', \
'BENCH_ALGO_EQUI_3N_1.dat' w l ls 2 title '$3N+1$',\
'BENCH_ALGO_EQUI_20N_1.dat' w l ls 3 title '$20N+1$'