# Description: This script reads the parquet files and prints the schema of the files.
import os
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import pyarrow.parquet as pq 

pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)

def list_directory_tree_with_os_walk(starting_directory):
    for root, directories, files in os.walk(starting_directory):
        print(f"Directory: {root}")
        for file in files:
            print(f"  File: {file}")

list_directory_tree_with_os_walk('.')

# load parcquet files into pandas dataframes
X_train_observed_a = pd.read_parquet('./data/A/X_train_observed.parquet')
X_train_observed_b = pd.read_parquet('./data/B/X_train_observed.parquet')
X_train_observed_c = pd.read_parquet('./data/C/X_train_observed.parquet')

# Load the metadata of the parquet files
metadata_a = pq.read_metadata('./data/A/X_train_observed.parquet')
metadata_b = pq.read_metadata('./data/B/X_train_observed.parquet')
metadata_c = pq.read_metadata('./data/C/X_train_observed.parquet')

# Get the schema of the parquet files
schema_a = metadata_a.schema
schema_b = metadata_b.schema
schema_c = metadata_c.schema

print("Schema for file A:")
print(schema_a)
print("\nSchema for file B:")
print(schema_b)
print("\nSchema for file C:")
print(schema_c)

# Load the data
file_path = './data/B/X_train_observed.parquet'
_df = pq.read_table(file_path).to_pandas()

# Inspect the data
print(_df.info())
print(_df.describe())
print(_df.head())