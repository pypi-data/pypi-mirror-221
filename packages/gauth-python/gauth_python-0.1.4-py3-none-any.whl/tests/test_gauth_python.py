from gauth_python.requests import GAuthPython
import gauth_python

def test_function():
    assert GAuthPython.code_issuance("exampleString", "exampleString")
    assert GAuthPython.token_issuance("exampleString","exampleString","exampleString","exampleString")
    assert GAuthPython.token_reissuance()
    assert GAuthPython.user_info()

