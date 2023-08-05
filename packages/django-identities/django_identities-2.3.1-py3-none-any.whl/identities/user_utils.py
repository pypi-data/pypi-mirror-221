import logging
from typing import Any, Dict, Tuple

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import SuspiciousOperation
from django.conf import settings

User = get_user_model()

logger = logging.getLogger(__name__)


def get_or_create_user(username: str, email: str) -> Tuple[AbstractUser, bool]:
    """Fetches an user or creates a new one.

    Lookup happens via email address (case insensitive).

    :param username: User name. Always specified.
    :param email: email address. Always specified but could be empty.
    :return: tuple of User, bool
    """
    if email:
        try:
            return User.objects.get(email__iexact=email), False
        except User.DoesNotExist:
            # In case of multiple entries (which should hardly happens),
            # exception is passed to caller
            pass
    return User.objects.create_user(username, email), True


def create_user(claims):
    """Return object for a newly created user account."""
    mapper = settings.CONFIG.oidc.mapper
    username = claims.get("preferred_username")
    if not username:
        return None
    email = claims.get(mapper.email, "")
    user, created = get_or_create_user(username, email)
    if not created:
        logger.info(
            "Local user with email '%s' found. Changing username from '%s' to '%s'.",
            email,
            user.username,
            username,
        )
        # Reset the password (federated users have 'None' password) and change username
        user.set_unusable_password()
        user.username = username
    user.first_name = claims.get(mapper.first_name, user.first_name)
    user.last_name = claims.get(mapper.last_name, user.last_name)
    user.profile.affiliation = ",".join(claims.get(mapper.affiliation, []))
    user.profile.affiliation_id = ",".join(claims.get(mapper.affiliation_id, []))
    user.save()
    return user


def update_user(user, claims):
    """Update existing user with new claims, if necessary, save, and return user"""
    mapper = settings.CONFIG.oidc.mapper
    user.first_name = claims.get(mapper.first_name, "")
    user.last_name = claims.get(mapper.last_name, "")
    user.email = claims.get(mapper.email, "")
    sep = ","
    new_affiliation = sep.join(claims.get(mapper.affiliation, []))
    new_affiliation_id = sep.join(claims.get(mapper.affiliation_id, []))
    user.profile.affiliation = new_affiliation
    user.profile.affiliation_id = new_affiliation_id
    user.save()
    return user


def user_from_claims(username_claim: str, claims: Dict[str, Any]):
    """Create or get user based on claims"""
    users = User.objects.filter(username=claims[username_claim])
    if len(users) == 1:
        return update_user(users[0], claims)
    if len(users) == 0:
        return create_user(claims)
    raise SuspiciousOperation("Multiple users returned")
