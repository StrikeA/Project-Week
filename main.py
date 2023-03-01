import numpy as np
import pandas as pd
import sklearn
import pickle
from sklearn import linear_model

homeasrs = float(input("What is the home Adjusted SRS"))
awayasrs = float(input("What is the away Adjusted SRS"))

pickle_in = open("BasketBall_Model.pickle", "rb")
linear = pickle.load(pickle_in)
test_data = np.array([[homeasrs, awayasrs]])
prediction = linear.predict(test_data)
print(prediction)
