# K-Mode Clustering

The K-Modes clustering partitions the data into K mutually exclusive clusters. Unlike K-Means which uses distances
between numbers K-Modes uses the number of mismatches between categorical values to decide how similar two data points
are. For example:

- Data point 1: ["red", "small", "round"]
- Data point 2: ["blue", "small", "square"]

Here there are 2 mismatches (color and shape) so these two are not very similar.

### Use K-Modes

When to use:
- Your dataset contains categorical variables like gender, color, brand etc.
- You're analyzing survey responses Yes/No, Male/Female etc.
