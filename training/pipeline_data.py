import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data():
        df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

        df.columns = [c.replace(" ", "_").lower() for c in df.columns]

        x = df.drop(columns=["species"])
        y = df["species"]

        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        X_train.to_csv("../data/X_train.csv", index=False)
        X_test.to_csv("../data/X_test.csv", index=False)
        y_train.to_csv("../data/y_train.csv", index=False)
        y_test.to_csv("../data/y_test.csv", index=False)

if __name__ == "__main__":
    prepare_data()