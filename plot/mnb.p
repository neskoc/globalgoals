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
set xrange [-1:16]
set yrange [0:1.15]

set xtics scale 0 ()
set ytics scale 0 nomirror
set grid y
set bmargin at screen 0.2
set tmargin at screen 0.9
set xtic auto
set ytic auto
set xlabel "Label (topic class)"

plot for [col=2:4] 'MultiNB.dat' using col:xtic(1) ti columnhead(col) #, \
#        '' u 5:xtic(1) axis x1y2
set term png
set output '../img/Report_MultinomialNB.png'
replot
set term qt 