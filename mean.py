import csv
import statistics

with open('data.csv', newline="") as f:
  reader = csv.reader(f)
  height_weight_data = list(reader)
  
height_weight_data.pop(0)
height = []
for h in height_weight_data:
    height.append(float (h[1]))

m = statistics.mean(height)
print (m)

mode = statistics.mode(height)
print (mode)

median = statistics.median(height)
print (median)