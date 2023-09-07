# add your code here

# Add imports to script

import pandas as pd
import zipfile


# open zipped file

# with zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as zip_ref:
#     zip_ref.extract('winemag-data-130k-v2.csv', 'data')

df = pd.read_csv('data/winemag-data-130k-v2.csv', index_col=0)

solution_data =  (df.groupby(['country']).points.agg(['count', 'mean'])).rename(columns={'mean': 'points'})


print(solution_data)


