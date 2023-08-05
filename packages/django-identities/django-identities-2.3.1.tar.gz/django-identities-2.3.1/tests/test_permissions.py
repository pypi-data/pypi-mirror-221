from unittest.mock import Mock

import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from rest_framework import permissions
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.test import APIRequestFactory

import identities.permissions as identities_permission
from identities.apps import APP_NAME
from identities.models import Profile
from identities.permissions import (
    get_group_manager_groups,
    has_group_manager_permission,
    has_group_manager_groups,
    IsGroupManagerRead,
    IsGroupManagerWrite,
    ObjectPermission,
)
from identities.tests.factories import GroupFactory
from tests.conftest import make_group_manager

NONSAFE_METHODS = ("POST", "PUT", "PATCH", "DELETE")
factory = APIRequestFactory()


class TestGroupManager:
    @pytest.fixture(autouse=True)
    def before_each(self, create_group_manager, user_factory):
        # pylint: disable=attribute-defined-outside-init
        self.managed_group = GroupFactory.create()
        self.group_manager = create_group_manager(self.managed_group)
        self.staff = user_factory(staff=True)
        # pylint: enable=attribute-defined-outside-init

    def test_get_group_manager_groups(self):
        assert get_group_manager_groups(self.group_manager)[0] == self.managed_group
        managed_group2 = GroupFactory.create()
        make_group_manager(self.group_manager, managed_group2)
        assert tuple(get_group_manager_groups(self.group_manager)) == (
            self.managed_group,
            managed_group2,
        )
        assert get_group_manager_groups(self.staff).count() == 0

    def test_has_group_manager_groups(self):
        assert has_group_manager_groups(self.group_manager) is True
        assert has_group_manager_groups(self.staff) is False
        make_group_manager(self.staff, self.managed_group)
        assert has_group_manager_groups(self.staff) is True

    def test_has_group_manager_permission(self):
        # only `group_manager` has group manager permission for `managed_group`
        assert (
            has_group_manager_permission(self.group_manager, self.managed_group) is True
        )
        assert has_group_manager_permission(self.staff, self.managed_group) is False
        # `group_manager` does NOT have group manager permission for all groups
        assert has_group_manager_permission(self.group_manager) is False


@pytest.mark.parametrize(
    "permission_obj, allowed_methods, forbidden_methods",
    (
        (IsGroupManagerRead(), ("GET", "HEAD"), ("PUT", "PATCH", "POST", "DELETE")),
        (IsGroupManagerWrite(), ("PUT", "PATCH"), ("GET", "HEAD", "POST", "DELETE")),
    ),
)
class TestIsGroupManager:
    @pytest.fixture(autouse=True)
    def before_each(self, create_group_manager, user_factory):
        # pylint: disable=attribute-defined-outside-init
        self.factory = RequestFactory()
        self.user = user_factory(basic=True)
        self.staff = user_factory(staff=True)
        self.managed_group_1, self.managed_group_2 = GroupFactory.create_batch(2)
        self.group_manager_1 = create_group_manager(self.managed_group_1)
        self.group_manager_2 = create_group_manager(self.managed_group_2)
        self.request = self.factory.request()
        # pylint: enable=attribute-defined-outside-init

    # pylint: disable=unused-argument
    def test_anonymous(self, permission_obj, allowed_methods, forbidden_methods):
        for method in allowed_methods:
            self.request.user = AnonymousUser()
            self.request.method = method
            assert permission_obj.has_permission(self.request, None) is False

    def test_user(self, permission_obj, allowed_methods, forbidden_methods):
        for method in allowed_methods:
            self.request.user = self.user
            self.request.method = method
            assert permission_obj.has_permission(self.request, None) is False

    def test_group_manager_own_group(
        self, permission_obj, allowed_methods, forbidden_methods
    ):
        for user, group in (
            (self.group_manager_1, self.managed_group_1),
            (self.group_manager_2, self.managed_group_2),
        ):
            for method in allowed_methods:
                self.request.user = user
                self.request.method = method
                assert permission_obj.has_permission(self.request, None) is True
                assert (
                    permission_obj.has_object_permission(self.request, None, group)
                    is True
                )

    def test_group_manager_other_group(
        self, permission_obj, allowed_methods, forbidden_methods
    ):
        for user, group in (
            (self.group_manager_1, self.managed_group_2),
            (self.group_manager_2, self.managed_group_1),
        ):
            for method in allowed_methods:
                self.request.user = user
                self.request.method = method
                assert permission_obj.has_permission(self.request, None) is True
                assert (
                    permission_obj.has_object_permission(self.request, None, group)
                    is False
                )

    def test_group_manager_forbidden_methods(
        self, permission_obj, allowed_methods, forbidden_methods
    ):
        for method in forbidden_methods:
            self.request.user = self.group_manager_1
            self.request.method = method
            assert permission_obj.has_permission(self.request, None) is False

    def test_staff(self, permission_obj, allowed_methods, forbidden_methods):
        self.request.user = self.staff
        for method in allowed_methods:
            self.request.method = method
            assert permission_obj.has_permission(self.request, None) is False

    # pylint: enable=unused-argument


class TestIsStaff:
    @pytest.fixture(autouse=True)
    def before_each(self, user_factory):
        # pylint: disable=attribute-defined-outside-init
        self.factory = RequestFactory()
        self.user = user_factory(basic=True)
        self.staff = user_factory(staff=True)
        self.staff.is_staff = True
        self.permission_obj = identities_permission.IsStaff()
        # pylint: enable=attribute-defined-outside-init

    def test_anonymous(self):
        request = self.factory.request()
        request.user = AnonymousUser()
        assert self.permission_obj.has_permission(request, None) is False

    def test_user(self):
        request = self.factory.request()
        request.user = self.user
        assert self.permission_obj.has_permission(request, None) is False

    def test_staff(self):
        request = self.factory.request()
        request.user = self.staff
        assert self.permission_obj.has_permission(request, None) is True


class TestIsStaffOrReadOnly:
    @pytest.fixture(autouse=True)
    def before_each(self, user_factory):
        # pylint: disable=attribute-defined-outside-init
        self.factory = RequestFactory()
        self.user = user_factory(basic=True)
        self.staff = user_factory(staff=True)
        self.permission_obj = identities_permission.IsStaffOrReadOnly()
        self.request = self.factory.request()
        # pylint: enable=attribute-defined-outside-init

    def test_anonymous(self):
        self.request.user = AnonymousUser()
        assert self.permission_obj.has_permission(self.request, None) is False

    def test_user(self):
        self.request.user = self.user
        for method in permissions.SAFE_METHODS:
            self.request.method = method
            assert self.permission_obj.has_permission(self.request, None) is True
        for method in NONSAFE_METHODS:
            self.request.method = method
            assert self.permission_obj.has_permission(self.request, None) is False

    def test_staff(self):
        self.request.user = self.staff
        for method in permissions.SAFE_METHODS + NONSAFE_METHODS:
            self.request.method = method
            assert self.permission_obj.has_permission(self.request, None) is True


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (permissions.SAFE_METHODS, True),
        (NONSAFE_METHODS, False),
    ),
)
def test_readonly(rf, test_input, expected, basic_user_auth):
    permission_obj = identities_permission.ReadOnly()
    request = rf.request()
    request.user = basic_user_auth
    for method in test_input:
        request.method = method
        assert permission_obj.has_permission(request, None) is expected


class TestObjectPermission:
    @pytest.mark.parametrize(
        "method", ("GET", "OPTIONS", "HEAD", "PUT", "PATCH", "DELETE")
    )
    def test_get_required_object_permissions(self, method):
        ObjectPermission().get_required_object_permissions(method, Profile)

    @pytest.mark.parametrize("method", ("POST", "FOO", "get"))
    def test_get_required_object_permissions_not_allowed_method(self, method):
        with pytest.raises(MethodNotAllowed):
            ObjectPermission().get_required_object_permissions(method, Profile)

    def test_has_permission_anonymous(self):
        request = factory.get("/")
        request.user = None
        assert ObjectPermission().has_permission(request, None) is False

    def test_has_permission_method_not_allowed(self, user_factory):
        request = factory.post("/")
        request.user = user_factory()
        with pytest.raises(MethodNotAllowed):
            ObjectPermission().has_permission(request, None)

    @pytest.mark.parametrize(
        "method", ("get", "options", "head", "put", "patch", "delete")
    )
    def test_has_permission_method_ok(self, user_factory, method):
        request = getattr(factory, method)("/")
        request.user = user_factory()
        assert ObjectPermission().has_permission(request, None) is True

    def test_has_object_permission(self, user_factory):
        request = factory.get("/")
        mock_user = Mock()
        request.user = mock_user
        profile = Profile(user=user_factory())
        ObjectPermission().has_object_permission(request, None, profile)
        mock_user.has_perms.assert_called_once_with(
            (f"{APP_NAME}.view_{profile.__class__._meta.model_name}",), profile
        )
