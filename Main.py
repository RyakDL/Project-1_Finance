import pandas as pd

#merge data files
AZ_Employment ="EMPLOYAZ.csv"
AZ_Assets = "AZTAST.csv"

# Read the data and the study results
AZ_Employment = pd.read_csv(AZ_Employment)
AZ_Assets = pd.read_csv(AZ_Assets)

# Combine the data into a single DataFrame
Combined_AZ = pd.merge(AZ_Employment, AZ_Assets, how ='right')

Combined_AZ