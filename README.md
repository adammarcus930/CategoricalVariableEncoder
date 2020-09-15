# CategoricalVariableEncoder
Project exploring a new method for handling categorical variables when trying to develop ML models.

The purpose of this project was to create a module that could encode categorical varialbles better than both One-Hot Encoding and Label Encoding. Both of those methods both had considerable drawbacks leading me to believe their was opportunity for a better method. The drawback with [Label Encoding](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) is although it contains the variables to a single column, it also creates an abritrary order between variables. [One-Hot Encoding] (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) does not have the issue of creating a false order but it has the potential to create hundreds of columns if there are too many variables. 

To solve this issue, I developed a module that would create an ordinal column which is correlated to the target variable. This way we can hold the variable to one column but the order is no longer arbitrary. 

## File Descrption

DSHelper/CatEncoder.py - Module that contains a function GetOrdinal which takes in a pandas dataframe(s) and an array of target variables as inputs and transforms the dataset(s) by replacing categorical values with approprately ordered numerical values.

CategoricalEarlyResearch.ipynb - Jupyter notebook used to explore different categorical encoding techniques. The dataset used came from [Kaggle challenge](https://www.kaggle.com/c/cat-in-the-dat) where the goal was to have users build a model off a dataset that was comprised of mostly categorical variables. After submitting my original attempt using get_dummies(One-Hot Encoding) and comparing it to my method from the CatEncoder.py I was able to imrpove my Kaggle score from 0.72451 to 0.7877. 

HousePrices.ipynb - This analysis came from another Kaggle challenge I had previously attempted. I wanted to see how my newly created module would potentially effect my previous work if I used GetOrdinal over the get_dummies method. This too turned out to be a succes lowering my previous error from: 0.15274 to 0.12891. This was a very good result for me because I previously had spent many hours trying to lower this error but failed.  This tells me that the the new method potentially is a viable option going forward. 

