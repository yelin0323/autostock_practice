import pandas as pd

s = pd.Series([0.0,3.6,2.0,5.8,4.2,8.0])
s.index = pd.Index([0.0,1.2,1.8,3.0,3.6,4.8])
s.index.name = 'MY_IDX'
s.name = 'MY_SERIES'

s[5.9] = 5.5

print(s)
print(s.index[-1])
print(s.values[-1])