from distutils.command.build_scripts import first_line_re
import pandas as pd
from functools import reduce

# Read the datasets using read_csv function
df_ind = pd.read_csv('../dataset/indian_unicorns.csv')
df_ind = df_ind.dropna(subset=['Company'])

df_all = pd.read_csv('../dataset/world_unicorns.csv')
df_all = df_all.dropna(subset=['Company'])

# Drop indian companies that are former or graduated unicorns
remove_form_grad = df_ind[df_ind['Company'].str.contains('\^')].index
df_ind.drop(remove_form_grad, inplace=True)
remove_form_grad = df_ind[df_ind['Company'].str.contains('\*')].index
df_ind.drop(remove_form_grad, inplace=True)

# Drop non matching columns
df_ind.drop(columns=['Entry Valuation^^ ($B)'], inplace=True)

# Rename the columns to stop duplications
df_ind.rename(columns={'Sector':'Industry', 'Entry':'Date Joined', 'Location':'City'}, inplace=True)

# Add 'India' as a country column to the dataframe
df_ind['Country'] = 'India'

# Find the number of common companies in for datasets
list_common_companies = list(reduce(set.intersection, map(set, [df_all.Company, df_ind.Company])))

# Drop rows with Indian companies
remove_india_index = df_all[ df_all['Country'] == 'India' ].index
df_all.drop(remove_india_index, inplace=True)

# Concatenate the two dataframes
df_world_all = df_all.append(df_ind, ignore_index=True)

df_world_all.to_csv('../dataset/consolidated_dataset.csv')