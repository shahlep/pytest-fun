from pytest import mark


@mark.body
class BodyTest:

    @mark.smoke
    def test_body_functions_as_expected(self):
        assert True
