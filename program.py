# 1. Import pandas
import pandas as pd

# 2. Define a function and return pd as a date range. For fridays, use FRI, for sundays, use SUN
def allfridays(year):
    return pd.date_range(start=str(year), end=str(year+1),
                         freq='W-FRI').strftime('%m/%d/%Y').tolist()
  
  # 3. Tell the function to execute on a given year and to apply its results on a number of weeks
allfridays(2019)[:52]

# Full program

import pandas as pd

def allfridays(year):
    return pd.date_range(start=str(year), end=str(year+1),
                         freq='W-FRI').strftime('%m/%d/%Y').tolist()
allfridays(2019)[:52]
