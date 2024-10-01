# -*- coding: utf-8 -*-
"""final project AIML

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18Tz0lRUbu1qeu-B_4Aa11AkoUs3jl9P3
"""

!pip install opencv-python
!pip install easyocr

import numpy as np
import pandas as pd
import cv2
import easyocr
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import math
import scipy.stats as stats

# Load the dataframe using pandas
prep = pd.read_csv('/content/Historical Product Demand.csv')

# If you actually have an image you can use the following
# prep = cv2.imread('/content/Historical Product Demand.csv')

prep.info

# Check for columns with categorical data
prep.select_dtypes(include='object').columns

prep.select_dtypes(include='number').columns

# Check for missing values in the DataFrame
prep.isnull()

!pip install scikit-learn # Install scikit-learn library
import pandas as pd
from sklearn.impute import SimpleImputer # Import the SimpleImputer class

# Assuming 'prep' is your DataFrame and you want to impute missing numerical values
imputer = SimpleImputer(strategy='mean') # Create an imputer object with desired strategy
numerical_cols = prep.select_dtypes(include='number').columns # Select numerical columns

# Check if there are any numerical columns before imputation
if len(numerical_cols) > 0:
    # Fit and transform the imputer on your data
    prep[numerical_cols] = imputer.fit_transform(prep[numerical_cols])
else:
    print("No numerical columns found in DataFrame")

prep # If you intended to display the DataFrame 'prep'

#OR

#prep['df'] # Only uncomment this if 'df' is a valid column in the DataFrame

prep['key'] = prep['Product_Code'].astype(str) + '_' + prep['Warehouse'].astype(str)
#Based on the available columns in the 'prep' DataFrame ('Product_Code', 'Warehouse', 'Product_Category', 'Date', 'Order_Demand'),
#the code was updated to concatenate 'Product_Code' and 'Warehouse' to create the 'key' column.
#If other columns need to be used, please replace 'Product_Code' and/or 'Warehouse' with the correct column names.

prep = prep.drop(['Product_Code', 'Warehouse', 'Product_Category', 'Date', 'Order_Demand'], axis=1)
# Changed the column names to match the existing columns in the 'prep' DataFrame.
# Please verify these are the columns you intended to drop.

prep.dataset = prep.groupby('key').sum() # Removed '.df' to directly reference the 'prep' DataFrame

prep # If you intended to display the DataFrame 'prep'

#OR

#prep['key'] # Only uncomment this if 'key' is a valid column in the DataFrame

prep # This will display the DataFrame 'prep'

prep['day_1'] = prep['key'].shift(-1) # Changed 'units_sold' to 'key'
prep['day_2'] = prep['key'].shift(-2) # Changed 'units_sold' to 'key'
prep['day_3'] = prep['key'].shift(-3) # Changed 'units_sold' to 'key'
prep['day_4'] = prep['key'].shift(-4) # Changed 'units_sold' to 'key'

prep # This will display the DataFrame 'prep'

df = prep.dropna() # Removed .df as it is not an attribute of a pandas DataFrame

# Convert 'day_1', 'day_2', 'day_3', 'day_4' to numeric
# if they are of object type.
for col in ['day_1', 'day_2', 'day_3', 'day_4']: # Removed 'key' from the list as it is non-numeric.
  if df[col].dtype == 'object':
    try:
      df[col] = pd.to_numeric(df[col])
    except ValueError:
      # Handle the exception, e.g., print an error message or replace non-numeric values
      print(f"Could not convert column {col} to numeric due to non-numeric values.")
      # Example: Replace non-numeric values with NaN
      df[col] = pd.to_numeric(df[col], errors='coerce')

df[:100].select_dtypes(include='number').plot(figsize=(12,8))

x1, x2, x3, x4, y = df['day_1'], df['day_2'], df['day_3'], df['day_4'], df['key'] # Changed 'units_sold' to 'key'
x1, x2, x3, x4, y = np.array(x1), np.array(x2), np.array(x3), np.array(x4), np.array(y)
x1, x2, x3, x4, y = x1.reshape(-1,1), x2.reshape(-1,1), x3.reshape(-1,1), x4.reshape(-1,1), y.reshape(-1,1)

split_percentage = 15
test_split = int(len(df)*(split_percentage/100))
x = np.concatenate((x1, x2, x3, x4), axis=1)
X_train,X_test,y_train,y_test = x[:-test_split],x[-test_split:],y[:-test_split],y[-test_split:]

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# Convert 'day_1', 'day_2', 'day_3', 'day_4' to numeric
# if they are of object type.
for col in ['day_1', 'day_2', 'day_3', 'day_4']: # Removed 'key' from the list as it is non-numeric.
  if df[col].dtype == 'object':
    try:
      df[col] = pd.to_numeric(df[col])
    except ValueError:
      # Handle the exception, e.g., print an error message or replace non-numeric values
      print

import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sine Wave")

# Show the plot
plt.show()

# Import necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Initialize the LabelEncoder
le = LabelEncoder()

# Fit the encoder to your training data and transform both training and testing data
y_train = le.fit_transform(y_train.ravel()) #

import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
plt.rcParams["figure.figsize"] = (12,8)

# Assuming df is your DataFrame
X = df.drop('key', axis=1) # Replace 'target_variable' with the name of your target variable column 'key'
y = df['key']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a model (example: RandomForestClassifier)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Generate predictions
y_pred = model.predict(X_test)

# Now you can plot the predictions
plt.plot(y_pred[-100:], label='Predictions')
plt.plot(y_test[-100:], label='Actual Sales')
plt.legend(loc="upper left")
plt.show()

import xgboost
from sklearn.preprocessing import LabelEncoder

# Initialize the LabelEncoder
le = LabelEncoder()

# Fit the encoder to your training data and transform both training and testing data
y_train = le.fit_transform(y_train) # Encode target variables

xgb_regressor = xgboost.XGBRegressor()
xgb_regressor.fit(X_train, y_train)

y_pred = xgb_regressor.predict(X_test)

import xgboost
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Initialize the LabelEncoder
le = LabelEncoder()

# Fit the encoder to your training data and transform both training and testing data
y_train = le.fit_transform(y_train) # Encode target variables

# Ensure y_test has the same categories as y_train and handle mismatches
y_test = pd.Series(y_test) # Convert y_test to a Pandas Series
y_test = y_test[y_test.isin(le.classes_)]

# Check if y_test is empty after filtering
if len(y_test) == 0:
    # Handle the case where y_test is empty, possibly by retraining the model or investigating the data
    print("Warning: y_test is empty after filtering. Retraining the model or investigating the data is recommended.")
    # Instead of retraining with the entire dataset, investigate why y_test is empty
    # This could indicate a problem with your data or how you are splitting it
else:
    # Transform y_test using the fitted encoder
    y_test = le.transform(y_test) # Encode target variables

    xgb_regressor = xgboost.XGBRegressor()
    xgb_regressor.fit(X_train, y_train)

    y_pred = xgb_regressor.predict(X_test) # Changed xgb to xgb_regressor

import matplotlib.pyplot as plt
plt.plot(y_pred[-100:], label='Predictions')
plt.plot(y_test[-100:], label='Actual Sales')
plt.legend(loc="upper left")
plt.show()

from sklearn.model_selection import RandomizedSearchCV

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 50, stop = 250, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(0, 120, num = 20)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
print(random_grid)

# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestRegressor()
# Random search of parameters, using 3 fold cross validation,
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 10, cv = 3, verbose=2, random_state=0, n_jobs = -1)

rf_random.fit(X_train, y_train)

rf_random.best_params_

best_random = rf_random.best_estimator_

y_pred = best_random.predict(X_test)

# Check the shapes of X_test and y_test
print(X_test.shape)
print(y_test.shape)

# If the shapes are inconsistent, identify the source of the mismatch and fix it.
# For example, if there is an extra row in X_test, you can remove it using:
X_test = X_test[:-1]

# Alternatively, if there is a missing row in y_test, you can investigate why it's missing and potentially impute it.

# After fixing the mismatch, re-run the score calculation:
print("R Sq. Score for Random Forest Regression :", best_random.score(X_test, y_test))
print("Adj. R Sq. Score for Random Forest Regression :", 1 - (1 - best_random.score(X_test, y_test) ) * ( len(y_test) - 1 ) / ( len(y_test) - X_test.shape[1] - 1 ))

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (30,8)
plt.plot(y_pred[500:800], label='Predictions')
plt.plot(y_test[500:800], label='Actual Sales')
plt.legend(loc="upper left")
plt.savefig('final.png')
plt.show()