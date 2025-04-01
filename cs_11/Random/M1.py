# Lst = [2,2,2, 4, 4, 4, 5, 5, 7, 9]
# using statistics, process there sub function - Mean, Median, Mode, Modes

import statistics
lst = [2,2,2, 4, 4, 4, 5, 5, 5, 7, 9]
print(statistics.mean(lst))
print(statistics.median(lst))
print(statistics.mode(lst))
print(statistics.multimode(lst))