# Application 6 by Ahmed Diaa
import matplotlib.pyplot as plt
import pandas as pd # type: ignore
import seaborn as sns # type: ignore

df = sns.load_dataset('iris')

sns.scatterplot( x ='sepal_length' , y ='sepal_width' , hue='species' , data=df)
plt.title('Scatter Plot : Sepal length vs Sepal width')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()