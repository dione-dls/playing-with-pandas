import pandas as pd

stats = {'Trade': [1,2,3,4],
         'Instrument': ['Stock', 'Bond', 'ETF', 'Option'],
         'Price': [34, 99, 2, 6],
         'Quantity': [9, 10, 4, 10],
         'Timestamp': ['18-Jul-2018', '18-Jul-2018', '18-Jul-2018', '18-Jul-2018']}
         
df = pd.DataFrame(stats)
print(df)