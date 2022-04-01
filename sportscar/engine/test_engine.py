from pytest import mark


@mark.engine
class EngineTest:
    @mark.integration
    def test_engine_functions_as_expected(self):
        assert True
