import os

import pandas as pd
import pytest


def test_data_preparation():
    assert os.path.isfile("../datasets/housing/housing.csv")

def test_load_data():
    try:
        df = pd.read_csv(r"../datasets/housing/housing.csv")
        df.shape
    except:
        assert False

def test_dist():
    assert os.path.isdir("../dist/")
    assert os.path.isfile("../dist/median_housing_value_prediction-0.3-py3-none-any.whl")
    assert os.path.isfile("../dist/median_housing_value_prediction-0.3.tar.gz")

def test_artifact_dir():
    assert os.path.isdir("../artifacts/")

def test_pickle_file():
    assert os.path.isfile("../artifacts/lin_reg_op.pkl")
