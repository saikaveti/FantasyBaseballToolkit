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

### Under/Over-Valued Players

##### Undervalued Players
This list is found using two separate methods that each generate two different lists of undervalued players that are appended together to find a complete list of undervalued players.

Method 2 inspired by similar method for pitchers.

###### Method 1
Found list of players that had a BABIP of less than .250, while still having an average of .230 or above. The low BABIP indicates that the player is simply just "unlucky" over the course of the span, while the AVG restriction maintains that the player should still be able to generate some form of reliable contact.

###### Method 2
This method was more complex and involved k-means clustering. I chose 5 different clusters that classified players based on ISO, AVG, and OPS. I then took the average of the RC27 of each of the players in each cluster. Within each cluster, I found a list of players that had good peripherals, but was not converting into counting stats. This list was generated by players who had an RC27 more than 10% less than the average RC27 in the cluster.

Example:
```
STATISTICS FOR LAST 200 DAYS
First Name    Last Name      AB    R    H    HR    RBI    SO    SB     BA    OBP    SLG    OPS
------------  -----------  ----  ---  ---  ----  -----  ----  ----  -----  -----  -----  -----
Evan          Gattis        348   45   82    23     70    85     1  0.236  0.295  0.483  0.777
Ryon          Healy         391   43   92    23     60    90     0  0.235  0.268  0.445  0.713
Ian           Kinsler       370   52   89    13     35    42    11  0.241  0.308  0.403  0.711
Joe           Panik         237   28   58     4     18    17     2  0.245  0.305  0.35   0.656
Joc           Pederson      306   50   75    18     46    57     1  0.245  0.322  0.513  0.835
Salvador      Perez         400   40   95    21     60    86     1  0.238  0.276  0.438  0.714
Travis        Shaw          397   58   98    24     69    79     2  0.247  0.338  0.479  0.817
Yangervis     Solarte       432   50  101    17     53    67     1  0.234  0.288  0.398  0.686
Kevin         Kiermaier     234   30   42     4     18    67     8  0.179  0.246  0.295  0.541
Johan         Camargo       332   47   87    13     57    71     0  0.262  0.344  0.446  0.79
Ian           Happ          306   48   74    13     34   131     5  0.242  0.362  0.422  0.784
Starling      Marte         421   63  116    17     57    89    28  0.276  0.319  0.463  0.782
Hunter        Renfroe       262   34   64    13     42    72     1  0.244  0.306  0.473  0.779
Nick          Williams      344   44   91    17     49    94     3  0.265  0.331  0.456  0.787
Jorge         Alfaro        295   31   74     8     29   120     2  0.251  0.311  0.39   0.7
Jose          Iglesias      401   39  106     5     48    44    14  0.264  0.306  0.389  0.695
Khris         Davis         433   69  110    34     95   125     0  0.254  0.329  0.55   0.879
Bryce         Harper        424   78  105    30     79   133     9  0.248  0.383  0.514  0.897
Ehire         Adrianza      236   30   57     5     23    68     4  0.242  0.302  0.377  0.679
Tim           Anderson      433   63  106    15     49   112    24  0.245  0.291  0.409  0.7
```
##### Overvalued Players
This list is found using two separate methods that each generate two different lists of overvalues players that are appended together to find a complete list of overvalues players. Very similar to the method of finding overvalued players.

Method 2 inspired by similar method for pitchers.

###### Method 1
Found list of players that had a BABIP of greater than .375. The high BABIP indicates that the player is simply just "lucky" over the course of the span.

###### Method 2
This method was more complex and involved k-means clustering. I chose 5 different clusters that classified players based on ISO, AVG, and OPS. I then took the average of the RC27 of each of the players in each cluster. Within each cluster, I found a list of players that had good peripherals, but was not converting into counting stats. This list was generated by players who had an RC27 more than 10% more than the average RC27 in the cluster.

Example:
```
STATISTICS FOR LAST 200 DAYS
First Name    Last Name      AB    R    H    HR    RBI    SO    SB     BA    OBP    SLG    OPS
------------  -----------  ----  ---  ---  ----  -----  ----  ----  -----  -----  -----  -----
Jorge         Alfaro        295   31   74     8     29   120     2  0.251  0.311  0.39   0.7
Harrison      Bader         256   47   73     9     25    80    12  0.285  0.354  0.453  0.808
Austin        Jackson       223   22   64     2     23    84     3  0.287  0.344  0.386  0.73
Aaron         Judge         372   70  106    26     61   137     6  0.285  0.398  0.548  0.947
Mallex        Smith         352   48  106     2     29    75    26  0.301  0.374  0.426  0.8
Christian     Yelich        433   84  134    19     61   112    14  0.309  0.372  0.52   0.891
Andrelton     Simmons       424   57  126     8     56    26     7  0.297  0.348  0.422  0.77
Mallex        Smith         352   48  106     2     29    75    26  0.301  0.374  0.426  0.8
Andrew        Benintendi    448   87  134    15     70    83    20  0.299  0.38   0.5    0.88
Rhys          Hoskins       411   71  106    25     77   113     5  0.258  0.369  0.511  0.88
Nick          Markakis      478   69  152    14     80    60     1  0.318  0.379  0.492  0.871
Jesse         Winker        281   38   84     7     43    46     0  0.299  0.405  0.431  0.836
Freddy        Galvis        455   45  108    10     52   112     6  0.237  0.297  0.363  0.659
Manuel        Margot        374   42   91     6     41    70    10  0.243  0.292  0.377  0.669
Carlos        Santana       423   64   92    17     67    76     2  0.217  0.352  0.395  0.747
George        Springer      432   74  107    19     58    93     6  0.248  0.332  0.431  0.763
Jose          Ramirez       442   85  133    37     91    57    27  0.301  0.412  0.636  1.048
Mike          Trout         372   82  115    30     60    97    21  0.309  0.459  0.624  1.083
```
Source: http://www.users.miamioh.edu/stephamd/papers/Baseball_Machine_Learning.pdf

### Baseball Hit Prediction

The inspiration for this project can be found here: https://www.mlb.com/apps/beat-the-streak

#### Getting Data Points
In order to get the data for this project, I pulled data from Fangraphs, Baseball Reference, as well as Statcast. I used the following API in order to do so:  https://github.com/jldbc/pybaseball

Once the data was obtained in the form of a BeautifulSoup table, I parsed through it, pulling data that I believed to be important for calculating this probability.

I decided on the following parameters:
1. H
2. BB
3. SB
4. SH
5. BA
6. SLG

Choosing Parameters:
This was one of the most challenging parts of the project. I had to generate a heat map in order to detect whether variables were related. Since I had 300 data points on average, and am only allowed 1 data parameter per 50 points, I was limited to 6 data constraints.

These variables are good for such an analysis because they are independent of each other, and represent an important aspect of Baseball.

1. H - Ability to put ball in play
2. BB - Plate Disciple
3. SB - Speed
4. SH - Avoiding a strikeout
5. BA - How often a batter gets a hit
6. SLG - How "good" a player's hits are

I then pulled whether or not the player got a hit on the given day, allowing me to get all the data needed to (hopefully) learn the parameters accurately.

#### Performing Regression
Once the data was read from a CSV file into dataframe object, I was able to perform Logistic Regression from then on.

I executed the following statement to generate the training and testing data: (With a 75/25 split in the data)
```
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .25, random_state=25)
```

In order to obtain the prediction train, I executed the following statement:
```
y_pred = LogReg.predict(X_test)
```

In order to obtain the confusion matrix and classification matrix, I executed the following command:
```
confusion_matrix(y_test, y_pred)
classification_report(y_test, y_pred)
```

#### Final Results
Correctly predicted the result with a 75% overall accurancy. The confusion matrix and the classification report are below:
```
 [35  5]
 [17 23]
             precision    recall  f1-score   support

          0       0.67      0.88      0.76        40
          1       0.82      0.57      0.68        40

avg / total       0.75      0.72      0.72        80
```


### Projections

##### Algorithm

##### Comparing to Previous Years

##### Acessing Projections
