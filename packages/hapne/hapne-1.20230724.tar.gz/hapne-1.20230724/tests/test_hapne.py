from hapne import hapne_ld, hapne_ibd
from configparser import ConfigParser
import pandas as pd
import numpy as np
import logging


def test_hapne_ld():
    config = ConfigParser()
    config.read("tests/files/const_hapne_ld.ini")
    config["CONFIG"]["nb_bootstraps"] = "10"
    hapne_ld(config)
    inferred_ne = pd.read_csv("tests/files/const_test_ld/HapNe/hapne.csv")["Q0.5"].values
    true_ne = np.ones_like(inferred_ne) * 20_000
    assert np.mean((inferred_ne - true_ne) / true_ne) < 0.01


def test_hapne_ld_fixed():
    config = ConfigParser()
    config.read("tests/files/const_hapne_ld_fixed.ini")
    config["CONFIG"]["nb_bootstraps"] = "10"
    hapne_ld(config)
    inferred_ne = pd.read_csv("tests/files/const_test_ld_fixed/HapNe/hapne.csv")["Q0.5"].values
    true_ne = np.ones_like(inferred_ne) * 20_000
    assert np.mean((inferred_ne - true_ne) / true_ne) < 0.01


def test_hapne_ibd_fixed():
    config = ConfigParser()
    config.read("tests/files/const_hapne_ibd_fixed.ini")
    config["CONFIG"]["nb_bootstraps"] = "10"
    hapne_ibd(config)
    inferred_ne = pd.read_csv("tests/files/const_test_ibd_fixed/HapNe/hapne.csv")["Q0.5"].values
    true_ne = np.ones_like(inferred_ne) * 20_000
    assert np.mean((inferred_ne - true_ne) / true_ne) < 0.01


def test_hapne_ibd():
    config = ConfigParser()
    config.read("tests/files/const_hapne_ibd.ini")
    config["CONFIG"]["nb_bootstraps"] = "10"
    hapne_ibd(config)
    inferred_ne = pd.read_csv("tests/files/const_test_ibd/HapNe/hapne.csv")["Q0.5"].values
    true_ne = np.ones_like(inferred_ne) * 20_000
    assert np.mean((inferred_ne - true_ne) / true_ne) < 0.01


if __name__ == "__main__":
    # set logging level to INFO
    logging.basicConfig(level=logging.INFO)
    test_hapne_ld()
    # test_hapne_ibd()
