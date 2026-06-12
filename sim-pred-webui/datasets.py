import pandas as pd
from sklearn.datasets import load_diabetes, fetch_california_housing, load_iris


def get_diabetes_data():
    return load_diabetes(as_frame=True).frame


def get_california_housing():
    return fetch_california_housing(as_frame=True).frame


def get_iris():
    return load_iris(as_frame=True).frame


def get_titanic_data():
    return pd.read_csv('data/titanic_train.csv')


ds_dict = {
    "titanic": get_titanic_data,
    "load_diabetes": get_diabetes_data,
    "load_iris": get_iris,
    "fetch_california_housing": get_california_housing,
}


def get_dataset_names():
    return ds_dict.keys()


def get_sample_dataset(name):
    if name in ds_dict:
        return ds_dict[name]()
    return None


if __name__ == '__main__':
    # print(get_sample_dataset("load_iris").head())
    print(get_dataset_names())
