import numpy as np
import pickle
import csv

# Dictionary
dict = {"HASRS": 0.0, "AASRS": 0.0, "HMOV": None}

homeasrs = float(input("What is the home Adjusted SRS? "))
awayasrs = float(input("What is the away Adjusted SRS? "))

dict["HASRS"] = homeasrs
dict["AASRS"] = awayasrs
print(dict)
# list of column names
field_names = ["HASRS", "AASRS", "HMOV"]

with open("Basket Ball Data.csv", "a") as csv_file:
    dict_object = csv.DictWriter(csv_file, fieldnames=field_names)

    dict_object.writerow(dict)

pickle_in = open("BasketBall_Model.pickle", "rb")
linear = pickle.load(pickle_in)
test_data = np.array([[homeasrs, awayasrs]])
prediction = linear.predict(test_data)
print(prediction)