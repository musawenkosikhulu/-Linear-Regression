# -*- coding: utf-8 -*-
"""Linear_Regression_Prac_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JzxOyr6U473zZweo3pKUeL1Vlu6DlYzZ

## Linear Regression Prac 1

This notebook will make use of Scikit-learn's Linear Regression class. The documentation is found here: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

Credits:

The notebooks on linear regression are modifications of various sources which include:
https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
https://medium.com/analytics-vidhya/linear-regression-using-python-ce21aa90ade6
https://www.kdnuggets.com/2019/03/beginners-guide-linear-regression-python-scikit-learn.html/2

## Various Python imports
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

"""## Load the dataset"""

diabetes = datasets.load_diabetes()

"""## Take a look at what has been downloaded"""

diabetes

"""## Print out the feature names"""

diabetes['feature_names']

"""## Take a look at the shape of the data"""

diabetes['data'].shape

"""## Take a look at the shape of the targets (what we are predicting for)"""

diabetes['target'].shape

"""## Select a training feature

In this case we will be using a single feature for training. The algorithm will then try map this feature to the targets. In this case we are randomly select the feature number 5, however, this might not be the best choice! Feature '5' corresponds to the feature 's2' in our dataset (look above at our mapping).

Typically, features are denoted as X and targets as Y (some authors will use 'y' instead).
"""

X = diabetes.data[:, 1]
y = diabetes['target']

"""## Check shape!"""

X.shape

X = X.reshape(-1,1)

X.shape

"""## Split into training and testing"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4278) # 70% training and 30% test

"""## Check the training features shape"""

X_train.shape

"""## Check the testing features shape"""

X_test.shape

"""## Define a linear regression model

Read the API: https://scikit-learn.org/stable/modules/linear_model.html
"""

model = LinearRegression()

"""## Look at what has just being initialised"""

model

"""## Train the model/fit the model"""

model.fit(X_train, y_train)

"""## Print the coefficient"""

model.coef_

"""## Print the intercept"""

model.intercept_

"""## The model

The model, given the above output, is as follows:

y = 149 + 381x

y = 149 + 381d1, d1 = feature 5

y = 149 d0 + 381 d1, d0 = 1, d1 = feature 5

## Apply the model to the testing features and get the predictions
"""

Y_pred = model.predict(X_test)

"""## Determine the performance of the model on the testing data

There are various options, but commonly used one include:

* mean squared error
* mean absolute error
* root mean squared error

There can be implemented using scikit-learn.

### Mean squared error
"""

mean_squared_error(y_test, Y_pred)

"""### Mean absolute error"""

mean_absolute_error(y_test, Y_pred)

"""### Root mean squared error"""

np.sqrt(mean_squared_error(y_test, Y_pred))

"""## Plot the line and the testing data"""

plt.scatter(X_test, y_test,  color='gray')
plt.title('Linear Regression')
plt.plot(X_test, Y_pred, color='red', linewidth=1)
plt.show()

"""## Task: determine which feature will result in the best performing model."""
