import numpy as np                # Import numpy library for numerical operations
import pandas as pd               # Import pandas library for data manipulation
import sklearn                    # Import sklearn library for machine learning models
import pickle                     # Import pickle library for saving models
from sklearn import linear_model  # Import linear_model from sklearn

data = pd.read_csv("Basket Ball Data.csv")   # Read the CSV file using pandas
data = data[["HASRS", "AASRS", "HMOV"]]      # Define the columns to be used
predict = "HMOV"                            # Define the dependent variable
X = np.array(data.drop([predict], axis=1))  # Define the independent variables as a numpy array
y = np.array(data[predict])                 # Define the dependent variable as a numpy array
best = 0                                    # Initialize the best accuracy score to 0

while best < 0.97:
    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.05)
    linear = linear_model.LinearRegression()  # Define the linear regression model
    linear.fit(x_train, y_train)             # Fit the model to the training data
    acc = linear.score(x_test, y_test)       # Calculate the accuracy score on the testing data

    if acc > best:
        best = acc                          # Update the best accuracy score
        print(best)
        with open("BasketBall_Model.pickle", "wb") as f:
            pickle.dump(linear, f)          # Save the model with the best accuracy score to a pickle file

print(best)                                  # Print the final best accuracy score
