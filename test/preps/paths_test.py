import pytest
import os
from compose.preps.paths import prepaths

@pytest.fixture
def fragment_dirname():
    prep_test_dir = os.path.dirname(__file__)
    return os.path.join(prep_test_dir, 'fixture')

def test_prepaths(fragment_dirname):
    path_fragnames = ['user_paths.yaml', 'admin_paths.yaml']
    expected_paths = ['/users/base', '/users/enterprise', '/admin']
    paths = prepaths(fragment_dirname, path_fragnames)
    
    assert len(paths) == len(expected_paths)
    
    for path in expected_paths:
        assert path in paths
