from pytest import mark


@mark.entertainment
class EntertainmentTest:
    @mark.smoke
    def test_entertainment_systems_functions_as_expected(self):
        assert True
