#!/usr/bin/gnuplot -persist

# Gnuplot script file for plotting data in file "training_set.dat"
# This file (gnuplot script): training_set.p
reset
set title 'Complete labeled dataset: Training and test'
set key autotitle columnheader
# set datafile separator ","
set datafile commentschars "#%"
set key title "Columns"
set key invert reverse Left outside
set style data histogram
set style histogram rowstacked
set style fill solid border -1
set boxwidth 0.8
set autoscale
unset log
unset label
# set xrange [0:16]
set yrange [0:105]

set xtics scale 0 ()
set ytics scale 0 nomirror
set grid y
set bmargin at screen 0.2
set tmargin at screen 0.9
set xtic auto
set ytic auto
set xlabel "Label (topic class)"

# Colors
array A[4]
A[2] = '#a6cee3'
A[3] = '#1f78b4'
A[4] = '#b2df8a'

plot for [col=2:4] 'training_set.dat' using col:xtic(1) lc rgb A[col] ti columnhead(col)
# plot 'test.dat' using 2:xtic(1),  '' using 2 title 'Col1', '' using 3 title 'Col2', '' using 4 title 'Col3'
# plot 'test.dat' using 2:xtic(1) title 'Col1', '' using 3 title 'Col2', '' using 4 title 'Col3'
set term png
set output '../img/training_set.png'
replot
set term qt 
