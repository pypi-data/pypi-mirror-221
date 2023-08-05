import pytest
from django.contrib.auth import get_user_model

from identities.models import Profile

User = get_user_model()


class TestProfile:
    test_input_expected = (
        (
            ("cnorris", "Chuck", "Norris", "cnorris@roundhouse.gov"),
            "Chuck Norris (cnorris@roundhouse.gov)",
        ),
        (
            (
                "CNORRIS@roundhouse.gov",
                None,
                None,
                "cnorris@roundhouse.gov",
            ),
            "CNORRIS@roundhouse.gov (ID: CNORRIS) (cnorris@roundhouse.gov)",
        ),
        (
            ("CNORRIS@roundhouse.gov", None, None, None),
            "CNORRIS@roundhouse.gov (ID: CNORRIS)",
        ),
    )

    @pytest.mark.parametrize("test_input, expected", test_input_expected)
    def test_display(self, test_input, expected):
        profile = Profile(
            user=User(
                username=test_input[0],
                first_name=test_input[1],
                last_name=test_input[2],
                email=test_input[3],
            ),
        )
        assert profile.display_name == expected

    def test_str(self):
        assert str(Profile(user=User(username="bob"))) == "Profile (bob)"
