import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
df=pd.read_csv('C:\\Users\\YOGINATH\\Downloads\\householdtask3.csv')
plt.bar(df['year'], df['tot_hhs'], color='yellow')
plt.title('Bar Chart of Year vs Total Households')
plt.xlabel('Year')
plt.ylabel('Total Households')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
plt.plot(df['year'], df['tot_hhs'], marker='*',color='orange')
plt.title('Line Chart of Year vs Total Households')
plt.xlabel('Year')
plt.ylabel('Total Households')
plt.grid(True)
plt.show()
plt.figure(figsize=(5, 3))
plt.scatter(df['year'], df['tot_hhs'], color='red', alpha=0.5)
plt.title('Scatter Plot of Year vs Total Households')
plt.xlabel('Year')
plt.ylabel('Total Households')
plt.grid(True)
plt.show()