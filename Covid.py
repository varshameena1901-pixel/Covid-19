import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("COVID clinical trials.csv")
df.head()
df.info()

# intial Data Exploration
# Dataset size
df.shape

#column type
df.dtypes

#Missing Value Analysis
#Check missing data

df.isnull().mean() * 100

#create country
df['Country'] = (
    df['Locations']
    .astype(str)
    .str.split(',')
    .str[-1]
    .str.strip()
)
df.columns

#Export clean data from python
df.to_csv("cleaned_clinical_trials.csv", index=False)



