# LinearRegressionML
Uses linear regression - a statistical approach to predict values and reduce errors associated with it for a particular dataset.

Dataset used - Auto insurance in Sweden

Source - https://www.kaggle.com/sunmarkil/auto-insurance-in-sweden-small-dataset/version/1

modules used : numpy,random,csv and math
___________________________________________
Contains line and dataset classes. Takes in a random stretch of data from the insurance data set(using csv.reader) as a training set and 
a testing set(dataset objects). Evaluates thir RMSE scores.
___________________________________________
Statistical formulae used:- 

To find intercept of the best fit line(c) : 

c = (Σx*Σ(xy) - Σy*Σx²) / ( (Σx)² -n*Σx² )

To find slope of the best fit line(m) : 

m = (Σx*Σy - n*Σ(xy)) / ( (Σx)² -n*Σx² )
     
To find RMSE : 

RMSE = sqrt(Σ{(y' - y)²}  /n)
___________________________________________
Outputs the RMSE score for the random data sets used. 

RMSE for whole dataset used as testing and training - 38.339
RMSE typically ranges between ~35.0 to ~60.0
Max value of criterion variable(y) = 422.22





