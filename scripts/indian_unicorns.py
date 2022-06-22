### Import required libraries
import urllib.request as urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np

### SCRAPPER TARGET URL
scrape_target = "https://www.ventureintelligence.com/Indian-Unicorn-Tracker.php"

### Get the client HTML and Parse the html
client_raw = urlopen.urlopen(scrape_target)
soup_html = soup(client_raw, 'html.parser')

### Get the table containing the required data
unicorn_content = soup_html.find('table', id="myTable")

### Find all rows in the extracted table
table_rows = unicorn_content.find_all('tr')

### Find all the column headers
temp_columns = unicorn_content.find_all('th')
table_col = []
for each in temp_columns:
    table_col.append(each.text)

### Find all the information inside the rows of the table
temp_row = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    temp_row.append(row)

### Convert the extracted table into a pandas dataframe
df_data = pd.DataFrame(temp_row, columns=table_col)

### Clean the data

# Drop columns not required
df_data.drop(['No'], axis=1, inplace=True)

# Rename the columns as required
df_data.rename(columns={'Select Investors  \nDownload\n': 'Select Investors'}, inplace=True)

# Convert the None values to np.nan, and drop the entirely empty rows
df_data.fillna(value=np.nan, inplace=True)
df_data.dropna(how='all', inplace=True)

df_data.to_csv('.\dataset\indian_unicorns_all_time.csv')