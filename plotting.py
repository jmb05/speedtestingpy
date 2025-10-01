import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
from datetime import datetime
import math

time_data = []
ping_data = []
jitter_data = []
up_data = []
down_data = []
 
for i in range(1, len(sys.argv)):
    with open(sys.argv[i], 'r', newline='\n') as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        for row in reader:
            if line_count != 0:
                time_data.append(datetime.fromtimestamp(float(row[0])))
                ping_data.append(float(row[1]))
                jitter_data.append(float(row[2]))
                down_data.append(int(row[10]) / 1000000)
                up_data.append(int(row[11]) / 1000000)
            line_count += 1

fig_length = -11.36 + 5.46 * math.log(len(time_data))
fig_length = max(6, fig_length)
print(fig_length)
plt.figure(figsize=[int(fig_length),6])
plt.plot(time_data, down_data)
plt.plot(time_data, up_data)
plt.legend(['down', 'up'])
plt.gcf().autofmt_xdate()
plt.savefig("bandwidth.svg")
plt.figure(figsize=[6,6])
plt.plot(time_data, ping_data)
plt.plot(time_data, jitter_data)
plt.legend(['ping', 'jitter'])
plt.savefig("ping_jitter.svg")

