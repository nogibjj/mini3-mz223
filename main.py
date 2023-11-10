import polars as pl


def load_data(file_path):
    dataframe = pl.read_csv(file_path, ignore_errors=True)
    return dataframe


if __name__ == "__main__":
    df = load_data("./assets/datasets/credit/train.csv")
    print(df.height)
    print(df.wid)
