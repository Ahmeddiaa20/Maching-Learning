# Application 4 by Ahmed Diaa do hists
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0,1,100) # normal function to have numbers from 0 to 100 after 1

plt.hist(data,bins=30,edgecolor='black') # bins the area of the table , edgecolor the color of the wall of the table
plt.title('Histogram of Data Distribution')# normal title
plt.xlabel('Valves')
plt.ylabel('Frequency')
plt.show()

mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data)

print(f"Mean = {mean_value}")
print(f"Median = {median_value}")
print(f"Deviation = {std_deviation}")
