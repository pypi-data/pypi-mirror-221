import os

from stdflow.path import Path


def setup():
    import datetime
    import os
    import random
    import shutil
    import string

    import pandas as pd

    if os.path.exists("./data"):
        shutil.rmtree("./data")

    os.mkdir("./data/")
    os.mkdir("./data/fr")
    os.mkdir("./data/fr/step_raw")
    os.mkdir("./data/fr/step_raw/v_1")
    os.mkdir("./data/fr/step_raw/v_1.2")
    os.mkdir("./data/fr/step_raw/v_2")
    os.mkdir("./data/fr/step_raw/v_12")
    # create empty file
    open("./data/fr/step_raw/v_0", "w").close()


setup()


def test_versions():
    path = Path("./data", path="fr", step_name="raw", version="last")
    assert (
        path.full_path == "./data/fr/step_raw/v_2/"
    ), f"src.full_path: {path.full_path}"

    path = Path("./data", path="fr", step_name="raw", version="first")
    assert (
        path.full_path == "./data/fr/step_raw/v_1/"
    ), f"src.full_path: {path.full_path}"


def test_from_ip_split():
    path = Path.from_input_params(
        data_root_path="./data",
        path="fr",
        step="raw",
        version="1",
        file_name="file.csv",
    )
    assert (
        path.full_path == "./data/fr/step_raw/v_1/file.csv"
    ), f"path.full_path: {path.full_path}"


def test_from_ip_split_wrong_input():
    path = Path.from_input_params(
        data_root_path="./data",
        path="fr",
        step="step_raw",
        version="v_1",
        file_name="file.csv",
    )
    assert (
        path.full_path == "./data/fr/step_raw/v_1/file.csv"
    ), f"path.full_path: {path.full_path}"


def test_from_ip_split_auto():
    path = Path.from_input_params(
        data_root_path="./data",
        path="fr",
        step="raw",
        version="first",
        file_name="file.csv",
    )
    assert (
        path.full_path == "./data/fr/step_raw/v_1/file.csv"
    ), f"path.full_path: {path.full_path}"


if __name__ == "__main__":
    test_versions()
    test_from_full_path_with_file()
    test_from_ip()
    test_from_ip_split()
    test_from_ip_split_wrong_input()
    test_from_ip_split_auto()
