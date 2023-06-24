import pandas as pd
df_series = {'1' : ['a','b','c'],
             '2' : ['b','c','d'],
             '3' : [2,3,'z']}

ex_df = pd.DataFrame(df_series)
print(ex_df)