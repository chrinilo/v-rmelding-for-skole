import try1
import pytest 

def test_mytest():
    with pytest.raises(SystemExit):
        try1.f()