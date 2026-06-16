import gradio as gr
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

DESCRIPTION = """
***Description:*** Logistic regression example with the titanic dataset. 

We use this model now because the core task requires binary classification: predicting whether a passenger survived (1) or perished (0).

Key points:
- Feature Engineering (Data Preprocessing)
- Imputation
- Encoding (Label and One-Hot encoding)
- Visualisation: Confusion Matrix
"""


def example_lr01():
    # header
    gr.Markdown("## <u>Titanic</u>", elem_classes="tight_layout")
    gr.Markdown(DESCRIPTION, elem_classes="tight_next")

    # 1
    gr.Markdown("### 1. Read Data")
    gr.Markdown("Here we read 2 datasets: **train** and **test** datasets from separate files.")
    train_df = pd.read_csv('../src/data/titanic_train.csv')
    test_df = pd.read_csv('../src/data/titanic_test.csv')
    gr.Dataframe(train_df[:5], elem_classes="tight_next")

    # 2
    gr.Markdown("### 2. Check duplications")
    gr.Markdown(
        f"Duplicates in Train Dataset is: {train_df.duplicated().sum()} ({100 * train_df.duplicated().sum() / len(train_df)}%)")
    gr.Markdown(
        f"Duplicates in Test Dataset is: {test_df.duplicated().sum()} ({100 * test_df.duplicated().sum() / len(test_df)}%)")

    # 3
    gr.Markdown("### 3. Check missing values")
    gr.Markdown(
        "As we see, there are missing values in this dataset. We will **impute** those values with the **mean**.")
    gr.Markdown("We also drop the unnecessary columns.")
    df_missing = pd.DataFrame({'Columns': train_df.isnull().sum().index,
                               'Number of missing values': train_df.isnull().sum().values})
    gr.Dataframe(df_missing, elem_classes="tight_next")

    # 3.b
    train_df = train_df.drop(['Cabin', 'Name', 'Ticket', 'Fare', 'PassengerId'], axis=1)
    test_df = test_df.drop(['Cabin', 'Name', 'Ticket', 'Fare', 'PassengerId'], axis=1)

    mean_imputer = SimpleImputer(strategy='mean')
    train_df['Age'] = mean_imputer.fit_transform(train_df[['Age']])
    test_df['Age'] = mean_imputer.fit_transform(test_df[['Age']])

    freq_imputer = SimpleImputer(strategy='most_frequent')
    train_df.iloc[:, :] = freq_imputer.fit_transform(train_df)
    test_df.iloc[:, :] = freq_imputer.fit_transform(test_df)

    # 4
    label_encoder = LabelEncoder()
    ordinal_cat_cols = ["Pclass", "SibSp", "Parch"]
    nominal_cat_cols = ["Sex", "Embarked"]

    train_df[ordinal_cat_cols] = train_df[ordinal_cat_cols].apply(label_encoder.fit_transform)
    test_df[ordinal_cat_cols] = test_df[ordinal_cat_cols].apply(label_encoder.fit_transform)
    train_df = pd.get_dummies(train_df, columns=nominal_cat_cols)
    test_df = pd.get_dummies(test_df, columns=nominal_cat_cols)

    gr.Markdown("### 4. Encoding values")
    gr.Markdown(f"Now we Label encode some categorical columns: {ordinal_cat_cols}")
    gr.Markdown(f"And we One-Hot encode the nominal categorical columns: {nominal_cat_cols}")
    gr.Dataframe(train_df[:5], elem_classes="tight_next")

    X = train_df.drop(columns=["Survived"])
    y = train_df["Survived"]

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    x_train_predicted = model.predict(x_train)
    x_test_predicted = model.predict(x_test)

    # 5
    a = accuracy_score(y_train, x_train_predicted) * 100
    b = accuracy_score(y_test, x_test_predicted) * 100

    gr.Markdown("### 5. Metrics", elem_classes="tight_layout")
    with gr.Row():
        gr.Label(f"{a:.2f}", label="Accuracy Score (Training data)")
        gr.Label(f"{b:.2f}", label="Accuracy Score (Testing data)")
        gr.Label(f"{precision_score(y_test, x_test_predicted):.2f}", label="Precision")
        gr.Label(f"{recall_score(y_test, x_test_predicted):.2f}", label="Recall")
        gr.Label(f"{f1_score(y_test, x_test_predicted):.2f}", label="F1 Score")

    # 6
    gr.Markdown("### 6. Confusion Matrix", elem_classes="tight_layout")
    gr.Markdown("I have seen better models than this.")

    fig, ax = plt.subplots(dpi=150, figsize=(4, 3))
    cm = confusion_matrix(y_test, x_test_predicted)
    sns.heatmap(cm, annot=True, fmt="g", cmap="summer")
    gr.Plot(value=fig)
