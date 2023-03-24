import numpy as np        # Import numpy library for numerical operations
import pickle            # Import pickle library for loading saved models
import csv               # Import csv library for writing data to a CSV file

# Create a dictionary with keys for the home and away Adjusted SRS values and home margin of victory
dict = {"HASRS": None, "AASRS": None, "HMOV": None}

# Prompt the user to enter the home and away Adjusted SRS values and store them in the dictionary
homeasrs = float(input("What is the home Adjusted SRS? "))
awayasrs = float(input("What is the away Adjusted SRS? "))
dict["HASRS"] = homeasrs
dict["AASRS"] = awayasrs

# Print the dictionary to the console
print(dict)

# Create a list of column names for the CSV file
field_names = ["HASRS", "AASRS", "HMOV"]

# Open the CSV file in append mode and create a dictionary writer object
with open("Basket Ball Data.csv", "a") as csv_file:
    dict_object = csv.DictWriter(csv_file, fieldnames=field_names)

    # Write the dictionary to the CSV file
    dict_object.writerow(dict)

# Load the saved linear regression model from the pickle file
pickle_in = open("BasketBall_Model.pickle", "rb")
linear = pickle.load(pickle_in)

# Create a numpy array with the home and away Adjusted SRS values
test_data = np.array([[homeasrs, awayasrs]])

# Use the linear regression model to make a prediction and store the result in a variable
prediction = linear.predict(test_data)

# Print the prediction to the console
print(prediction)
