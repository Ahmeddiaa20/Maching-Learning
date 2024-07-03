# Application 3 with Ahmed Diaa // Using numpy and Matplotlib
import numpy as np
import matplotlib.pyplot as plt
data = [12,14,18,20,16]

percent_25 = np.percentile(data,25)
percent_50 = np.percentile(data,50)
percent_75 = np.percentile(data,75)

print (f"25th Percentile : {percent_25}")
print (f"50th Percentile (Median): {percent_25}")
print (f"75th Percentile : {percent_25}")

plt.boxplot(data)
plt.title('Bocplot with percentiles ')
plt.xlabel('Data')
plt.ylabel('Values')
plt.show()