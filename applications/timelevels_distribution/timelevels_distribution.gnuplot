#@@@@@@@@@@@@@@@@@@@@@@@@@@@
# paper plot, initialization
#@@@@@@@@@@@@@@@@@@@@@@@@@@@
# global style definition
set style line 2 linetype -1 linewidth 1 lc rgb "gray70"
set style line 3 linetype 1 linewidth 2
set style line 4 linetype 3 linewidth 3
set style line 6 linetype 4 linewidth 3


# global parameters
set terminal epslatex standalone
set xrange [0:1]

set size square

# legend definition
set key reverse Left left spacing 1.5

#@@@@@@@@@@@@@@@@@@@@@@@@@@@
# figure
#@@@@@@@@@@@@@@@@@@@@@@@@@@@

# set labels
set xlabel 'Evenly spaced time levels'
set ylabel 'Non-evenly spaced time levels'

set output 'NONEQUI_TIMELEVELS_POSITION_F1.tex'
plot x w l ls 2 notitle,\
'TIMELEVELS_DISTRIBUTION_F1.dat' u 1:2 w linespoints ls 6 title 'EQUI $\kappa(A) = 33.1$', \
'TIMELEVELS_DISTRIBUTION_F1.dat' u 1:3 w linespoints ls 4 title 'APFT $\kappa(A) = 3.8$', \
'TIMELEVELS_DISTRIBUTION_F1.dat' u 1:4 w linespoints ls 3 title 'OPT $\kappa(A) = 1.1$'

# set labels
set output 'NONEQUI_TIMELEVELS_POSITION_F2.tex'
plot x w l ls 2 notitle,\
'TIMELEVELS_DISTRIBUTION_F2.dat' u 1:2 w linespoints ls 6 title 'EQUI $\kappa(A) = 33.1$', \
'TIMELEVELS_DISTRIBUTION_F2.dat' u 1:3 w linespoints ls 4 title 'APFT $\kappa(A) = 3.8$', \
'TIMELEVELS_DISTRIBUTION_F2.dat' u 1:4 w linespoints ls 3 title 'OPT $\kappa(A) = 1.1$'