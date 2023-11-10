[![CI](https://github.com/nogibjj/mini3-mz223/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mini3-mz223/actions/workflows/cicd.yml)

# Week 3 Mini-project: Polors Descriptive Statistics Script

## Overview
This repository contains a Python script (`main.py`) for loading a CSV file into a Polars DataFrame and printing its shape. The script is an introductory example of using pandas for data analysis, specifically for understanding the structure of a dataset.

## What's `Polars`
Polars is an in-memory DataFrames library written in Rust with bindings for Python, similar to pandas. It is designed to be fast and efficient, capable of handling large datasets with ease. Polars leverages Rust's performance and safe concurrency to provide speedy operations on tabular data.

Here are some key features of Polars:
- `Lazy Computations`: Polars can perform operations lazily, meaning that it builds a computation plan before executing it, which can optimize the overall performance by merging and simplifying operations where possible.
- `Speed and Memory Efficiency`: Because it is written in Rust, Polars can handle data processing very quickly, often outperforming pandas, especially on large datasets.
- `API Similarity to pandas`: For Python users, Polars provides an API that is somewhat similar to pandas, making it easier for those familiar with pandas to transition to using Polars.
- `Multithreading`: Polars is designed to efficiently use all available CPU cores for parallel data processing, leading to significant performance gains.
- `Expression System`: Polars features a powerful expression system that allows for the creation of custom operations and helps in building complex queries.
- `Interoperability`: Polars can interact with other Python data tools, making it possible to integrate within the existing data processing pipelines that use NumPy, pandas, or other libraries.

## Installation

Before running the script, ensure you have Python installed on your system. This script was written using Python 3.9.7, but it should be compatible with any Python 3.x version.

Additionally, you'll need to install pandas. It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install pandas
```

Usage
To execute the script, run the following command from the root of the repository:
```
python main.py
```
The script will load the data from ./assets/datasets/credit/train.csv and print the shape of the DataFrame to the console.

Project Structure
* `main.py`: The main script file.
* `assets/datasets/credit/train.csv`: The dataset file (not included in the repository).
* `requirements.txt`: The file listing the necessary Python dependencies.
* `test_main.py`: Contains unit tests for main.py to ensure the load function works correctly.

## Continuous Integration with GitHub Actions

The project uses GitHub Actions, employing the following commands:

- `make install`: Installs project dependencies.
- `make test`: Runs unit tests.
- `make format`: Formats the code according to the specified style.
- `make lint`: Checks the code for potential errors and style issues.
![Image](./images/WechatIMG792.jpg)

### CI Results
[Please click here](https://github.com/nogibjj/mini3-mz223/actions)
