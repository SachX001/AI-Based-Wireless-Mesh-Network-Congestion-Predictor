import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_and_prepare_data():

    data = pd.read_csv("dataset.csv")

    encoder = LabelEncoder()

    data["congestion"] = encoder.fit_transform(data["congestion"])

    X = data.drop("congestion", axis=1)

    y = data["congestion"]

    return X, y, encoder