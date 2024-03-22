import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


USAhousing = pd.read_csv('data/USA_Housing.csv')
print(USAhousing.head())


print(USAhousing.describe())


print(USAhousing.columns)

print(sns.pairplot(USAhousing))


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

lm = LinearRegression()

