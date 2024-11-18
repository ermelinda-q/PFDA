# PFDA - Week 7
# Lab 1.
# Checking the relation between the windspeed and the month in knock Airport.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv",
skiprows=19)
#print(df.head(3))

# Checking if there is any correlation between the month and mean temperature.
corrtemp = df["month"].corr(df["meant"])
print(corrtemp)

# creating a dataframe with the values we need.
cleandf = df[["month","wdsp"]]

# Drop the NA values.
# cleandf.dropna(inplace=True) DOESN'T WORK!!!


cleandf['wdsp']= cleandf.loc[:,('wdsp')].replace(' ', np.nan)






