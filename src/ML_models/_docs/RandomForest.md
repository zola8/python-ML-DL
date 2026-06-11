# Random Forest

A **Decision Tree** is a supervised learning algorithm used for both classification and regression tasks.
It has a hierarchical tree structure which consists of a root node, branches, internal nodes and leaf nodes.
It works like a flowchart that helps in making step-by-step decisions.

**Random Forest** is a machine learning algorithm that uses many decision trees to make better predictions.
Each tree looks at different random parts of the data and their results are combined by voting for
classification or averaging for regression.

### Working of Random Forest Algorithm

- Create Many Decision Trees: The algorithm makes many decision trees each using a random part of the data.
  So every tree is a bit different.
- Pick Random Features: When building each tree it doesn’t look at all the features (columns) at once.
  It picks a few at random to decide how to split the data. This helps the trees stay different from each other.
- Each Tree Makes a Prediction
- Combine the Predictions

### Random Forest Hyperparameter Tuning using Sklearn

**n_estimators**: It defines the number of trees in the forest.
More trees typically improve model performance but increase computational cost.

**random_state**=42: Ensures reproducible results.

**oob_score**=True: Uses out-of-bag samples to estimate model performance.

**max_features**: Limits the number of features to consider when splitting a node. This helps control overfitting.

**max_depth**: Controls the maximum depth of each tree. 
A shallow tree may underfit while a deep tree may overfit. So choosing right value of it is important.

**max_leaf_nodes**: Limits the number of leaf nodes in the tree hence controlling its size and complexity. 
None means it takes an unlimited number of nodes.

