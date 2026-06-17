# Naive Bayes Classifiers

Naive Bayes is a ML classification algorithm that predicts the category of a data point using probability.
It assumes that all features are independent of each other.

- We are trying to classify something, we assume that each feature (or piece of information) in the data
  does not affect any other feature.
- Continuous features are normally distributed.
- If a feature is discrete, then it is assumed to have a multinomial distribution within each class.
- The data should not contain any missing values.
- All features are equally important.

Disadvantages:

- May assign zero probability to unseen events, leading to poor generalization.

### Types of Naive Bayes Model

- Gaussian Naive Bayes (GNB)
- Multinomial Naive Bayes (MNB)
- Bernoulli Naive Bayes (BNB)
- Complement Naive Bayes (CNB)

**Gaussian Naive Bayes:**

- It is suitable for continuous data where features follow a Gaussian distribution.
- It assumes a Gaussian distribution for the likelihood.
- It is commonly used in tasks involving continuous data such as medical diagnosis, fraud detection and weather
  prediction.
- The likelihood of each feature is modelled using the Gaussian distribution.
- It may not perform well on non-normal or sparse data.

**Multinomial Naive Bayes:**

- It is specially designed for discrete data particularly text data.
- It assumes features and represent its counts like word counts.
- It is commonly used in NLP for document classification tasks.
- The likelihood of each feature is calculated using the multinomial distribution.
- It is more efficient when the number of features is very high like in text datasets with thousands of words.

**Bernoulli Naive Bayes:**

- Typically used when the data is binary and it models the occurrence of features using Bernoulli distribution.
- It is used for the classification of binary features such as 'Yes' or 'No', '1' or '0', 'True' or 'False' etc.
- Each message is represented using binary features indicating the presence (1) or absence (0) of a word.
- Bernoulli Naive Bayes is used for spam detection, text classification, Sentiment Analysis and used to determine
  whether a certain word is present in a document or not.

**Complement Naive Bayes:**
- Specifically designed to improve classification performance on imbalanced datasets and text classification tasks.

