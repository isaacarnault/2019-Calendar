Ignore below outputs if programs ran correctly.<br>
If you begin in `Python` using `Jupyter` these are what you should get:

<details><summary>Program</summary>
<p>
  
```python
# Full program
import pandas as pd

def allfridays(year):
    return pd.date_range(start=str(year), end=str(year+1),
                         freq='W-FRI').strftime('%m/%d/%Y').tolist()
allfridays(2019)[:52]
```

</p>
</details>

[![isaac-arnault-dates-estimator-using-python.png](https://i.postimg.cc/fLDnCnVF/isaac-arnault-dates-estimator-using-python.png)](https://postimg.cc/CZPQM2HH)

<details><summary>Exercise solution </summary>
<p>
  
```python
# Full program
import datetime

date = datetime.datetime.now()
date.year
date.month
weekNumber = date.today().isocalendar()[1]
date.day

print(date)
print(date.year)
print(date.month)
print(weekNumber)
print(date.day)
```

</p>
</details>

[![isaac-arnault-exercise-solution.png](https://i.postimg.cc/C17y6PDK/isaac-arnault-exercise-solution.png)](https://postimg.cc/MMnrnY9k)
