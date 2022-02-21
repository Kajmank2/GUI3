set style data lines
set xrange [0:10]
set yrange [-0.5:10.5]
set xlabel "iteration"
set ylabel "min batt / av batt / max batt"
#set key at 95,0.5
#set label "a=0.1" at 5,0.9
#set label "CA: 100 x 100 cells" at 40,1.05
#set label "num of experiments=50" at 200,110
#set label "8 single runs" at 200,110
#set label "b=1.6" at 40,80
plot 'CA_result.txt' using 1:4 with lines lc 1 lw 3 title "min batt",\
'CA_result.txt' using 1:5 with lines lc 4 lw 3 title "av batt",\
'CA_result.txt' using 1:6 with lines lc 7 lw 3 title "max batt"

