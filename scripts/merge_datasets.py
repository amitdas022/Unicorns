from distutils.command.build_scripts import first_line_re
import pandas as pd
from functools import reduce

# Read the datasets using read_csv function
df_ind = pd.read_csv('../dataset/indian_unicorns_all_time.csv')
df_ind = df_ind.dropna(subset=['Company'])

df_all = pd.read_csv('../dataset/world_unicorns.csv')
df_all = df_all.dropna(subset=['Company'])

print(df_all.shape, df_ind.shape)

# Drop non matching columns
df_ind.drop(columns=['Entry Valuation^^ ($B)'], inplace=True)

# Rename the columns to stop duplications
df_ind.rename(columns={'Sector':'Industry', 'Entry':'Date Joined', 'Location':'City'}, inplace=True)

# Add 'India' as a country column to the dataframe
df_ind['Country'] = 'India'

# Find the number of common companies in for datasets
list_common_companies = list(reduce(set.intersection, map(set, [df_all.Company, df_ind.Company])))

# Concatenate the two dataframes
df_world_all = df_all.append(df_ind, ignore_index=True)

# Remove duplicates
# df_world_all = df_world_all.drop_duplicates(subset=["Company"].lower(), keep=False)
# df_duplicates = df_world_all[df_world_all.duplicated(subset=['Company', 'Country'], keep='first')]
df_duplicates = df_world_all[df_world_all.duplicated(subset=['Company', 'Country', 'Industry'])]

print(df_duplicates)
print(df_world_all.shape)