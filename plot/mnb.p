#!/usr/bin/gnuplot -persist

# Gnuplot script file for plotting data in file "MultiNB.data"
# This file (gnuplot script): mnb.p
reset
set title 'Classification report: Multinomial Naïve Bayes'
set key autotitle columnheader 
# set datafile separator ","
set datafile commentschars "#%"
set key title "Columns"
set key noinvert box
set style data histogram
set style fill solid border -1
set style histogram cluster gap 1.5 
set boxwidth 1.2
set autoscale
unset log
unset label
# set xrange [-1:16]
set yrange [0:1.15]
set y2range [0:40]

set xtics scale 0 ()
set ytics scale 0 nomirror
set y2tics 10, 10
set grid y
set bmargin at screen 0.2
set tmargin at screen 0.9
set xtic auto
set ytic auto
set xlabel "Label (topic class)"

# Colors
array A[5]
A[2] = '#a6cee3'
A[3] = '#1f78b4'
A[4] = '#b2df8a'
A[5] = '#33a02c'

plot for [col=2:4] 'MultiNB.dat' using col:xtic(1) lc rgb A[col]  ti columnhead(col) , \
        '' u 5:xtic(1) axis x1y2 lc rgb A[5]  ti columnhead(5)
set term png
set output '../img/Report_MultinomialNB.png'
replot
set term qt 
