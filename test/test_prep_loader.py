import pytest
from compose.prep_loader import PrepLoader 

@pytest.fixture
def prep_loader():
    return PrepLoader()

@pytest.mark.parametrize('prepname', ['prepaths', 'precomponents'])
def test_getprep_exists(prep_loader, prepname):
    prep = prep_loader.getprep(prepname)
    assert prep != None

def test_getprep_not_exist(prep_loader):
    with pytest.raises(NotImplementedError):
        prep_loader.getprep('prenone')