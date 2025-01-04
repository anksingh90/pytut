import statistics
data = [2, 4, 4, 4, 5, 5, 7, 9]

mean = statistics.mean(data) # avg
print(f"Mean: {mean}")  # Output: Mean: 5.0

median = statistics.median(data) # middle value
print(f"Median: {median}")  # Output: Median: 4.5

data2 = [2, 4, 4, 5, 5, 7, 9] #odd number of elements

mode = statistics.mode(data) # most frequent value
print(f"Mode: {mode}")  # Output: Mode: 4

modes = statistics.multimode(data) # list of all modes
print(f"Modes: {modes}")  # Output: Modes: [1, 2, 3]