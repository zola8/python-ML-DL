# Hyperparameter tuning using GridSearchCV

**GridSearchCV** and **RandomizedSearchCV** are used to perform hyperparameter tuning.
(CV = Cross-Validation)

First let's use GridSearchCV to obtain the best parameters for the model 
that exhaustively searches through all possible combinations of parameters provided in the param_grid.

**param_grid**: A dictionary containing hyperparameters and their possible values. 
GridSearchCV will try every combination of these values to find the best-performing set of hyperparameters.

**grid_search.fit**(X_train, y_train): This trains the model on the training data (X_train, y_train) 
for every combination of hyperparameters defined in param_grid.


# Hyperparameter Tuning using RandomizedSearchCV

RandomizedSearchCV performs a random search over a specified parameter grid. 
It randomly selects combinations and evaluates the model often leading to faster results especially when there are many hyperparameters.

