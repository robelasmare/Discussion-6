import imp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df= pd.read_csv('Life Expectancy Data.csv')

#Used to show missing values for each column
df.isna().sum()

#used to see the outfitters in the dataset
column = 'Adult Mortality'
q1 = df[column].quantile(0.25)
q3 = df[column].quantile(0.75)
iqr = q3 - q1
upper_boundary = q3 + 1.5 * iqr
lower_boundary = q1 - 1.5 * iqr
df[(df[column] < lower_boundary) | (df[column] > upper_boundary)][column]

# Used to see the outfitters in the dataset
column = 'infant deaths'
q1 = df[column].quantile(0.25)
q3 = df[column].quantile(0.75)
iqr = q3 - q1
upper_boundary = q3 + 1.5 * iqr
lower_boundary = q1 - 1.5 * iqr
df[(df[column] < lower_boundary) | (df[column] > upper_boundary)][column]

#Used the scatter plot to see the correlation of the datasets and the outfitters for Adult Mortality and Country
plt.scatter(df['Adult Mortality'], df['Country'])
plt.rcParams['figure.figsize'] = [70, 100]
plt.show()

#Used to graph bar graph
plt.bar(df['Adult Mortality'], df['Country'])
plt.title("Bar Chart")
plt.xlabel('Country')
plt.ylabel('Adult Mortality')
plt.rcParams['Adult Mortality'] = [10, 10]


# Scatter plat with infant dath  with HIV/AIDS 
plt.scatter(df['infant deaths'], df['Country'])
plt.rcParams['figure.figsize'] = [30, 100]
plt.show()



# Setting X and Y labels 
plt.bar(df['infant deaths'], df['Country'])
plt.title("infant deaths vs Country")
plt.xlabel('infant deaths')
plt.ylabel('Country')
plt.show()

#ploting a bar chart
plt.bar(df['Country'], df['Adult Mortality'])
plt.title("Bar Chart")
plt.xlabel('Country')
plt.ylabel('Adult Mortality')
#used to plot scatter graph
plt.scatter(df['Adult Mortality'], df['Country'])
plt.rcParams['figure.figsize'] = [30, 100]
plt.show()

#used to plot histogram for Adult Mortality
df_copy=df.copy()
df_copy['Adult Mortality'].plot.hist()
plt.rcParams['figure.figsize'] = [1, 1]

#THANK YOU !!!
 

