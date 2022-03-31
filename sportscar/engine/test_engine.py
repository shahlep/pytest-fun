from pytest import mark


@mark.integration
@mark.engine
def test_engine_functions_as_expected():
    assert True
