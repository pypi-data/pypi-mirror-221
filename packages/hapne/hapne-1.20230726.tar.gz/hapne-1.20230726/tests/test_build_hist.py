from configparser import ConfigParser
from hapne.ibd import build_hist_in_parallel
import pandas as pd
import numpy as np


def test_build_hist():
    config = ConfigParser()
    config.read("tests/files/const_hapne_ibd.ini")
    build_hist_in_parallel(0, config)
    converted_files = pd.read_csv(
        "tests/files/const_test_ibd/IBD/chr1.from752721.to121475791.ibd.hist",
        sep="\t", header=None)
    answer = pd.read_csv("tests/files/const_test_ibd/test.ibd.hist",
                         sep="\t", header=None)
    assert np.sum(np.abs(converted_files[2] - answer[2]).values) == 0


if __name__ == "__main__":
    test_build_hist()
