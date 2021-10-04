# !pip install brewer2mpl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")


url='D:\study_notebook\Top 50 matplotlib Visualizations\orders.xlsx'
url.replace('\\','\\\\')

#prepare data
df=pd.read_excel(url)
y=df.iloc[:,6]
x=range(1,len(y)+1)
plt.plot(x,y,color='tab:blue')
plt.ylim(10,280)
plt.grid(axis='both')
x_location=x[::4]
x_labels=[i+1 for i in range(len(x_location))]
plt.xticks(x_location,x_labels,horizontalalignment='center')
plt.title('orders during Janurary')
plt.xlabel('day')
plt.ylabel('orders')
plt.gca().spines["top"].set_alpha(0.0)    
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.0)    
plt.gca().spines["left"].set_alpha(0.3)   
plt.show()
