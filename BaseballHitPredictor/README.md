# Baseball Hit Prediction

The inspiration for this project can be found here: https://www.mlb.com/apps/beat-the-streak

## Getting Data Points
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

## Performing Regression
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

## Final Results
Correctly predicted the result with a 75% overall accurancy. The confusion matrix and the classification report are below:
```
 [35  5]
 [17 23]
             precision    recall  f1-score   support

          0       0.67      0.88      0.76        40
          1       0.82      0.57      0.68        40

avg / total       0.75      0.72      0.72        80
```
