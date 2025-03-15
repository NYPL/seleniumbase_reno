import pytest
from examples.nypl_utility.utility import NyplUtils


class Abc(NyplUtils):
    """
    This test is intentionally designed to fail for testing GitHub Actions purposes.
    """

    @pytest.mark.test
    def test_abc(self):
        print("test_abc()\n")

        # assert title
        self.assert_true(2 + 2 == 5, "2 + 2 not equal 5")
