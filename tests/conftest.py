import zipfile
import pickle

from collections import namedtuple
from os import path, getenv
from random import randint

import pytest
import yaml


TEST_DATA = "data"
TEST_NET = "CREMI_DUNet_pretrained_new"

NNModel = namedtuple('NNModel', ['config', 'model', 'state'])

@pytest.fixture
def datadir(tmpdir):
    confdir = path.dirname(__file__)
    return path.join(confdir, TEST_DATA)


def _tuple_to_list(dct):
    for key, val in dct.items():
        if isinstance(val, dict):
            _tuple_to_list(val)
        elif isinstance(val, tuple):
            dct[key] = list(val)

    return dct


@pytest.fixture
def nn_sample(tmpdir, datadir):
    tmp_model_dir = tmpdir / "models"
    tmp_model_dir.mkdir()

    model_zip_fn = path.join(datadir, f"{TEST_NET}.zip")
    with zipfile.ZipFile(model_zip_fn, 'r') as model_zip:
        model_zip.extractall(tmp_model_dir)
        nn_dir = path.join(tmp_model_dir, TEST_NET)

    file_contents = []
    with open(path.join(nn_dir, 'tiktorch_config.yml')) as file:
        conf = yaml.load(file)
        _tuple_to_list(conf)
        file_contents.append(conf)

    for filename in ['model.py', 'state.nn']:
        with open(path.join(nn_dir, filename), 'rb') as file:
            file_contents.append(file.read())

    return NNModel(*file_contents)


@pytest.fixture
def srv_port():
    return getenv("TEST_TIKTORCH_PORT", randint(5500, 9999))


@pytest.fixture
def tiny_model(datadir):
    with open(path.join(datadir, "tiny_models.py"), "r") as f:
        model_file = pickle.dumps(f.read())

    return {
        "model_file": model_file,
        "model_state": b"",
        "optimizer_state": b"",
        "config": {
            "model_class_name": "TestModel0",
            "inference_batch_size": 100,
            "optimizer_config": {
                "method": "Adam"
            }
        }
    }
