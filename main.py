import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model

data = pd.read_csv("Basket Ball Data.csv")
# Use pandas to read the csv
data = data[["HMOV", "HASRS", "AASRS"]]
# Define columns being used
predict = "HMOV"
# defining predict as home margin of error
X = np.array(data.drop([predict], axis=1))
y = np.array(data[predict])
best = 0
for _ in range(5):
    # training model a bunch of times and taking the best one
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    if acc > best:
        acc = best
        print(best)
        with open("possum_model.pickle", "wb") as f:
            pickle.dump(linear, f)
    # printing best accuracy and saving model

pickle_in = open("possum_model.pickle", "rb")
linear = pickle.load(pickle_in)
# loading the best model and doing a final test
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
# printing the intercept and coefficients
predictions = linear.predict(x_test)
# predicting the home margin of victory
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
# printing each of the predictions
