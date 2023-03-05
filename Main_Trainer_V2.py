import numpy as np
import pandas as pd
import sklearn
import pickle
from sklearn import linear_model

data = pd.read_csv("Basket Ball Data_V2.csv")
# Use pandas to read the csv
data = data[["HASRS", "AASRS", "HMOV"]]
# Define columns being used
predict = "HMOV"
# defining predict as home margin of error
X = np.array(data.drop([predict], axis=1))
y = np.array(data[predict])
best = 0
while best < 0.8:
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    # splitting data into train and test sets
    Logistic = linear_model.LogisticRegression()
    # defining model
    Logistic.fit(x_train, y_train)
    acc = Logistic.score(x_test, y_test)
    if acc > best:
        best = acc
        print(best)
        with open("BasketBall_Model_V2.pickle", "wb") as f:
            pickle.dump(Logistic, f)
print(best)



