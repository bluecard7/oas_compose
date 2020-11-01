import pytest
import os
from compose.preps.components import precomponents

@pytest.fixture
def fragment_dirname():
    prep_test_dir = os.path.dirname(__file__)
    return os.path.join(prep_test_dir, 'fixture')

def test_components(fragment_dirname):
    component_fragnames = [
        'users_component.yaml',
        'error_component.yaml',
        'param_components.yaml',
    ]
    expected_components = {
        'schemas': ['User', 'Error'], 
        'parameters': ['offsetParam', 'limitParam']
    }
    components = precomponents(fragment_dirname, component_fragnames)

    assert len(components) == len(expected_components)
    for component_type, modelnames in expected_components.items():
        assert component_type in components
        models = components[component_type]
        assert len(models) == len(modelnames)
        
        for modelname in modelnames:
            assert modelname in models
