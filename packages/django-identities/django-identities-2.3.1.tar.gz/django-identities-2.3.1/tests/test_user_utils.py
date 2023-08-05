import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from identities.user_utils import create_user, update_user


User = get_user_model()

CREATION_CLAIMS = {
    "preferred_username": "906726174130@identity.ch",
    "given_name": "Bob",
    "family_name": "Smith",
    "email": "bob@example.org",
    "linkedAffiliation": ["member@sciences.ch", "staff@sciences.ch"],
    "linkedAffiliationUniqueID": ["987321@sciences.ch", "24680@university.ch"],
}


def create_bob(
    affiliation="member@hospital.ch,staff@hospital.ch",
    affiliation_id="1234567@zuerich.ch,7654321@university.ch",
) -> AbstractUser:
    user = User.objects.create_user(username="bob", email="bob@example.org")
    user.profile.affiliation = affiliation
    user.profile.affiliation_id = affiliation_id
    return user


@pytest.mark.django_db
def test_create_user():
    user_created = create_user(CREATION_CLAIMS)
    user_db = User.objects.get(username="906726174130@identity.ch")
    assert user_created == user_db
    assert user_created.username == "906726174130@identity.ch"
    assert user_created.first_name == "Bob"
    assert user_created.last_name == "Smith"
    assert user_created.email == "bob@example.org"
    assert user_created.profile.affiliation == "member@sciences.ch,staff@sciences.ch"
    assert (
        user_created.profile.affiliation_id == "987321@sciences.ch,24680@university.ch"
    )
    assert create_user({}) is None


@pytest.mark.django_db
def test_from_local_to_federated():
    user_db = create_bob()
    assert user_db.username == "bob"
    assert user_db.first_name == ""
    assert user_db.last_name == ""
    assert user_db.profile.affiliation == "member@hospital.ch,staff@hospital.ch"
    assert user_db.profile.affiliation_id == "1234567@zuerich.ch,7654321@university.ch"
    user_updated = create_user(CREATION_CLAIMS)
    assert user_updated.username == "906726174130@identity.ch"
    assert user_updated.first_name == "Bob"
    assert user_updated.last_name == "Smith"
    assert user_updated.profile.affiliation == "member@sciences.ch,staff@sciences.ch"
    assert (
        user_updated.profile.affiliation_id == "987321@sciences.ch,24680@university.ch"
    )


@pytest.mark.django_db
def test_federation_overwrites_local():
    user_db = create_bob()
    user_db.first_name = "Robert"
    user_db.last_name = "Martin"
    user_db.save()
    user_updated = create_user(CREATION_CLAIMS)
    assert user_updated.username == "906726174130@identity.ch"
    assert user_updated.first_name == "Bob"
    assert user_updated.last_name == "Smith"


@pytest.mark.django_db
def test_update_user_notification():
    user_db = create_bob()
    old_affiliation = user_db.profile.affiliation
    old_affiliation_id = user_db.profile.affiliation_id
    assert old_affiliation == "member@hospital.ch,staff@hospital.ch"
    assert old_affiliation_id == "1234567@zuerich.ch,7654321@university.ch"
    user_updated = update_user(
        user_db,
        {k: v for k, v in CREATION_CLAIMS.items() if k != "preferred_username"},
    )
    assert User.objects.get(username="bob") == user_updated
    assert user_updated.username == "bob"
    assert user_updated.first_name == "Bob"
    assert user_updated.last_name == "Smith"
    assert user_updated.email == "bob@example.org"
    # Affiliation has changed
    new_affiliation = "member@sciences.ch,staff@sciences.ch"
    new_affiliation_id = "987321@sciences.ch,24680@university.ch"
    assert user_updated.profile.affiliation == new_affiliation
    assert user_db.profile.affiliation == new_affiliation
    assert user_updated.profile.affiliation_id == new_affiliation_id
    assert user_db.profile.affiliation_id == new_affiliation_id


# pylint: disable=unused-argument
@pytest.mark.parametrize(
    "old_affiliation,new_affiliation,called",
    (
        ("", "", False),
        (None, "", False),
        ("", None, False),
        ("", "staff@sciences.ch", True),
        ("staff@sciences.ch", None, True),
        ("member@sciences.ch", "member@sciences.ch", False),
        (
            "staff@sciences.ch,member@sciences.ch",
            "staff@sciences.ch,member@sciences.ch",
            False,
        ),
        (
            "member@sciences.ch,staff@sciences.ch",
            "staff@sciences.ch,member@sciences.ch",
            False,
        ),
        ("student@sciences.ch,staff@sciences.ch", "staff@sciences.ch", False),
        (
            "student@sciences.ch,staff@sciences.ch",
            "staff@sciences.ch,member@sciences.ch",
            False,
        ),
        (
            "student@zuerich.ch,staff@sciences.ch",
            "student@sciences.ch,member@zuerich.ch",
            False,
        ),
        ("student@sciences.ch,staff@sciences.ch", "student@zuerich.ch", True),
        ("student@sciences.ch,student@zuerich.ch", "student@zuerich.ch", True),
    ),
)
@pytest.mark.django_db
def test_update_user(old_affiliation, new_affiliation, called):
    user_db = create_bob(old_affiliation)
    assert user_db.profile.affiliation == old_affiliation

    def empty_if_none(value):
        return value if value is not None else ""

    user_updated = update_user(
        user_db,
        {
            "linkedAffiliation": new_affiliation.split(",") if new_affiliation else [],
        },
    )
    # Affiliation has changed
    assert user_updated.profile.affiliation == empty_if_none(new_affiliation)
    assert user_db.profile.affiliation == empty_if_none(new_affiliation)
