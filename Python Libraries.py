

/*  http://pandas.pydata.org/pandas-docs/stable/10min.html */






>>>import matplotlib.pyplot as plt
>>> import numpy as np
>>> import pandas as pd
>>> s=pd.Series([1,3,5,np.nan,6,8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64







>>> df2 = pd.DataFrame({ 'A' : 1.,
...                      'B' : pd.Timestamp('20130102'),
...                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
...                      'D' : np.array([3] * 4,dtype='int32'),
...                      'E' : pd.Categorical(["test","train","test","train"]),
...                      'F' : 'foo' })
>>> df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo







>>> dates = pd.date_range('20130101',periods=10)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')




>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
>>> df
                   A         B         C         D
2013-01-01 -0.350060  0.509905 -0.888772  0.227829
2013-01-02 -0.128081 -0.876101  0.979286 -0.242199
2013-01-03 -0.242162 -0.531289 -0.233312  1.119337
2013-01-04 -0.625415 -0.388526  0.150249  0.251634
2013-01-05 -0.664839  0.837856  0.939270  0.443708
2013-01-06  0.555092  0.098832 -1.069560  1.085499




>>> df.T
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A   -0.350060   -0.128081   -0.242162   -0.625415   -0.664839    0.555092
B    0.509905   -0.876101   -0.531289   -0.388526    0.837856    0.098832
C   -0.888772    0.979286   -0.233312    0.150249    0.939270   -1.069560
D    0.227829   -0.242199    1.119337    0.251634    0.443708    1.085499




>>> df.index
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')




>>> df.head()
                   A         B         C         D
2013-01-01 -0.350060  0.509905 -0.888772  0.227829
2013-01-02 -0.128081 -0.876101  0.979286 -0.242199
2013-01-03 -0.242162 -0.531289 -0.233312  1.119337
2013-01-04 -0.625415 -0.388526  0.150249  0.251634
2013-01-05 -0.664839  0.837856  0.939270  0.443708




>>> df.tail()
                   A         B         C         D
2013-01-02 -0.128081 -0.876101  0.979286 -0.242199
2013-01-03 -0.242162 -0.531289 -0.233312  1.119337
2013-01-04 -0.625415 -0.388526  0.150249  0.251634
2013-01-05 -0.664839  0.837856  0.939270  0.443708
2013-01-06  0.555092  0.098832 -1.069560  1.085499




>>> df.columns
Index(['A', 'B', 'C', 'D'], dtype='object')



>>> df.values
array([[-0.35006039,  0.50990481, -0.88877167,  0.22782946],
       [-0.1280812 , -0.87610053,  0.97928632, -0.24219944],
       [-0.24216219, -0.53128903, -0.23331178,  1.11933735],
       [-0.62541488, -0.38852645,  0.15024898,  0.25163443],
       [-0.66483878,  0.83785628,  0.93927008,  0.44370836],
       [ 0.55509209,  0.09883154, -1.06956036,  1.08549943]])





>>> df.describe()
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean  -0.242578 -0.058221 -0.020473  0.480968
std    0.444029  0.656081  0.877451  0.531791
min   -0.664839 -0.876101 -1.069560 -0.242199
25%   -0.556576 -0.495598 -0.724907  0.233781
50%   -0.296111 -0.144847 -0.041531  0.347671
75%   -0.156601  0.407136  0.742015  0.925052
max    0.555092  0.837856  0.979286  1.119337





>>> df.sort_index(axis=1, ascending=False)
                   D         C         B         A
2013-01-01  0.227829 -0.888772  0.509905 -0.350060
2013-01-02 -0.242199  0.979286 -0.876101 -0.128081
2013-01-03  1.119337 -0.233312 -0.531289 -0.242162
2013-01-04  0.251634  0.150249 -0.388526 -0.625415
2013-01-05  0.443708  0.939270  0.837856 -0.664839
2013-01-06  1.085499 -1.069560  0.098832  0.555092





>>> df.loc[dates[0]]
A   -0.350060
B    0.509905
C   -0.888772
D    0.227829
Name: 2013-01-01 00:00:00, dtype: float64




>>> df.loc[:,['A','B']]
                   A         B
2013-01-01 -0.350060  0.509905
2013-01-02 -0.128081 -0.876101
2013-01-03 -0.242162 -0.531289
2013-01-04 -0.625415 -0.388526
2013-01-05 -0.664839  0.837856
2013-01-06  0.555092  0.098832

