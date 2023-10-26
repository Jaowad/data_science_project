import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def check_missing_values(df):
    missing_values = df.isnull().sum()

    print(missing_values)

    pass 


def check_duplicate_rows(df):
    # Check for duplicate rows
    duplicate_rows = df[df.duplicated()]

    # Print duplicate rows
    print("Duplicate Rows:")
    print(duplicate_rows)
    pass


def check_outliers(df):
    pass


def check_class_imbalance(df):
    pass


def check_correlation(df):

    pass


def check_distribution(df):
    pass


def check_target_distribution(df):
    pass


def check_feature_target_distribution(df):
    pass