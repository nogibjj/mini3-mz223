from main import load_data
import polars as pl


def test_load_data():
    # Path to the CSV file
    file_path = "./assets/datasets/credit/train.csv"

    # Load the data
    df = load_data(file_path)

    # Check that a Polars DataFrame is returned
    assert isinstance(df, pl.DataFrame)

    # Check that the DataFrame is not empty

    # Check the shape of the DataFrame. Polars uses height and width instead of shape
    assert df.height == 100000
    assert df.width == 28
