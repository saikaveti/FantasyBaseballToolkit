# FantasyBaseballToolkit

This project aims to create a library of tools relating to Fantasy Baseball. The features listed below will be added as more features are added.

### Player Statistic Retrieval

##### Find a single player's data for yesterday, last 7 days, last month, and year to date.
Example:
```
FINDING YESTERDAY'S DATA:
First Name    Last Name      AB    R    H    HR    RBI    SO    SB    BA    OBP    SLG    OPS
------------  -----------  ----  ---  ---  ----  -----  ----  ----  ----  -----  -----  -----
Paul          Goldschmidt     4    1    1     0      0     3     0  0.25    0.4   0.25   0.65

FINDING LAST WEEKS'S DATA:
First Name    Last Name      AB    R    H    HR    RBI    SO    SB     BA    OBP    SLG    OPS
------------  -----------  ----  ---  ---  ----  -----  ----  ----  -----  -----  -----  -----
Paul          Goldschmidt    12    1    2     0      0     8     0  0.167  0.286  0.167  0.452

FINDING LAST MONTH'S DATA:
First Name    Last Name      AB    R    H    HR    RBI    SO    SB     BA    OBP    SLG    OPS
------------  -----------  ----  ---  ---  ----  -----  ----  ----  -----  -----  -----  -----
Paul          Goldschmidt    93   11   29     5     12    26     1  0.312  0.407  0.516  0.924

FINDING YEAR TO DATE'S DATA:
First Name    Last Name      AB    R    H    HR    RBI    SO    SB     BA    OBP    SLG    OPS
------------  -----------  ----  ---  ---  ----  -----  ----  ----  -----  -----  -----  -----
Paul          Goldschmidt   360   61  100    21     52   113     3  0.278  0.384  0.528  0.912
```
### Player Comparison

##### A tool to easily compare various players across different statistical categories
Example:
```
STATISTICS FOR LAST 14 DAYS
First Name    Last Name      AB    R    H    HR    RBI    SO    SB     BA    OBP    SLG    OPS
------------  -----------  ----  ---  ---  ----  -----  ----  ----  -----  -----  -----  -----
J.D.          Martinez       29    8    8     2      6     9     0  0.276  0.382  0.552  0.934
Paul          Goldschmidt    35    2   10     1      1    12     1  0.286  0.375  0.4    0.775
```
##### A way to find players that are performing similarly to another player over a certain day range.
Example:
```
Finding players similar to PAUL GOLDSCHMIDT over the past 30 days.

STATISTICS FOR LAST 30 DAYS
First Name    Last Name      AB    R    H    HR    RBI    SO    SB     BA    OBP    SLG    OPS
------------  -----------  ----  ---  ---  ----  -----  ----  ----  -----  -----  -----  -----
Paul          Goldschmidt    93   11   29     5     12    26     1  0.312  0.407  0.516  0.924
Asdrubal      Cabrera        83   12   24     5     12    19     0  0.289  0.372  0.518  0.89
Derek         Dietrich       85   20   26     5     11    25     1  0.306  0.406  0.529  0.935
Juan          Soto           87   15   24     4     14    21     1  0.276  0.4    0.46   0.86
```
Additional Information:
The list can be tuned with a parameter that specifies how many categories have to be similar.
```
#Finds players with similar stats in 9 different categories
similarPlayers.find_similar_players(9)
```
##### A ranked list of players based on a single statistical category (OPG)
Example:
```
STATISTICS FOR LAST 200 DAYS
First Name    Last Name      AB    R    H    HR    RBI    SO    SB     BA    OBP    SLG    OPS
------------  -----------  ----  ---  ---  ----  -----  ----  ----  -----  -----  -----  -----
Mookie        Betts         310   79  110    23     51    45    18  0.355  0.444  0.677  1.121
Mike          Trout         341   71  104    25     50    86    15  0.305  0.451  0.595  1.046
Jose          Ramirez       368   70  112    30     72    49    20  0.304  0.401  0.639  1.04
J.D.          Martinez      357   72  116    29     80    95     2  0.325  0.392  0.639  1.03
Max           Muncy         232   45   63    22     42    67     2  0.272  0.41   0.599  1.009
Nolan         Arenado       352   66  110    25     72    74     2  0.313  0.395  0.597  0.992
Matt          Carpenter     332   64   92    25     53    90     0  0.277  0.386  0.593  0.979
Jesus         Aguilar       280   50   82    25     71    86     0  0.293  0.369  0.618  0.987
Eugenio       Suarez        306   50   95    19     71    71     1  0.31   0.396  0.565  0.961
Manny         Machado       373   48  118    24     65    51     8  0.316  0.39   0.571  0.961
Aaron         Judge         360   68  103    26     61   132     6  0.286  0.398  0.558  0.956
Freddie       Freeman       367   60  116    16     64    80     6  0.316  0.405  0.534  0.939
Andrew        Benintendi    356   69  108    14     57    71    17  0.303  0.387  0.52   0.907
Francisco     Lindor        396   86  116    25     63    74    15  0.293  0.371  0.563  0.934
Alex          Bregman       378   67  107    20     64    55     8  0.283  0.387  0.529  0.916
Shin-Soo      Choo          358   55  104    18     44    94     3  0.291  0.401  0.497  0.899
Paul          Goldschmidt   364   62  101    21     52   116     3  0.277  0.384  0.525  0.909
Trevor        Story         372   51  109    20     68   105    13  0.293  0.357  0.554  0.911
J.T.          Realmuto      282   47   88    12     45    57     1  0.312  0.366  0.535  0.901
Jose          Altuve        395   63  130     9     45    54    14  0.329  0.394  0.466  0.86
Joey          Votto         346   55   99     9     50    64     1  0.286  0.418  0.436  0.854
Nick          Markakis      375   55  121    10     62    46     1  0.323  0.387  0.485  0.872
Gleyber       Torres        218   30   64    15     42    61     2  0.294  0.35   0.555  0.905
Scooter       Gennett       358   60  115    16     63    76     2  0.321  0.372  0.514  0.885
Brandon       Belt          300   44   86    14     43    70     2  0.287  0.383  0.487  0.87
```

Source: http://vixra.org/pdf/1205.0104v1.pdf 

### Player Projections (Start of Season vs. Current Performance)

##### Projections (Current Performance, Rest of Season, Current + Rest, Start of Season)
