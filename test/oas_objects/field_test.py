import pytest
from compose.oas_objects.field import FieldDesc

states = [
    (FieldDesc(), 'False', False), 
    (FieldDesc(True), 'True', True)
]

@pytest.mark.parametrize('desc, repr_str, required', states)
def test_field_desc_state(desc, repr_str, required):
    assert repr(desc) == repr_str
    assert desc.bare() == required
