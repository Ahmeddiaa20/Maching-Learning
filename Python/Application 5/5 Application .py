#Application 5 by Ahmed Diaa
import matplotlib.pyplot as plt
import numpy as np

exam_scores = np.random.normal(70,10,100) # normal function to have numbers from 0 to 100 after 1

plt.hist(exam_scores,bins=30,edgecolor='black') # bins the area of the table , edgecolor the color of the wall of the table
plt.title('Distribution of Exam')# normal title
plt.xlabel('Valves')
plt.ylabel('Frequency')
plt.show()

