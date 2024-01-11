# **Bagging**

Methods such as Decision Trees, can be prone to overfitting on the training set which can lead to wrong predictions on new data.

Bootstrap Aggregation (bagging) is a ensembling method that attempts to resolve overfitting for classification or regression problems.
Bagging aims to improve the accuracy and performance of machine learning algorithms.
It does this by taking random subsets of an original dataset, with replacement, and fits either a classifier (for classification) or regressor (for regression) to each subset. 
The predictions for each subset are then aggregated through majority vote for classification or averaging for regression, increasing prediction accuracy
