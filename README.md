# CategoricalVariableEncoder
Project exploring a new method for handling categorical variables when trying develop ML models.

The purpose of this project was to create a module that could encode categorical varialbles better than both One-Hot Encoding and Label Encoding. The previous method both had considerable drawbacks which I have always found frustrating. Label Encoding is able to create a single column but it also creates an order between variables where there isn't one. One-Hot Encoding does not have the issue of creating a false order but it has the potential to create hundreds of columns if there are too many variables. 

To solve this issue, I developed a module that would create an ordinal column which is correlated to the target variable. This way we can hold the variable to one column but the order is no longer arbitrary.  
