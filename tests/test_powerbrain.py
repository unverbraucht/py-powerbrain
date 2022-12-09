import pytest
import requests
import json
from os import path

from powerbrain import Powerbrain

def read_file_to_json(base_path, version, fname):
    result = {}
    result[fname] = None
    full_path = path.join(base_path, version, f"{fname}.json")
    if path.exists(full_path):
        with open(full_path) as f:
            result[fname] = json.load(f)
    return result

def setup_requests_mock(ResponseVersion, requests_mock):
    for key in ResponseVersion:
        requests_mock.get(f'mock://powerbrain/cnf?cmd={key}', json=ResponseVersion[key])

TEST_DIR = path.join(path.dirname(path.realpath(__file__)), 'responses')

@pytest.fixture(params=['1.12.0', '1.14.0'])
def ResponseVersion(request):
    responses = read_file_to_json(TEST_DIR, request.param, 'get_params') | \
        read_file_to_json(TEST_DIR, request.param, 'get_dev_info') | \
        read_file_to_json(TEST_DIR, request.param, 'get_dev_types')   
    return responses

def test_params(ResponseVersion, requests_mock):
    setup_requests_mock(ResponseVersion, requests_mock)
    pb = Powerbrain('mock://powerbrain')
    pb.connect()
    assert pb.meta['title'] == 'Title'

def test_status(requests_mock, ResponseVersion):
    setup_requests_mock(ResponseVersion, requests_mock)
    pb = Powerbrain('mock://powerbrain')
    pb.connect()
    dev_info = pb.get_dev_info()
    assert dev_info['loadmgr_disabled'] == False
    assert dev_info['devices']['E1'] != None
    assert dev_info['devices']['E1']['attached_device'] != None

