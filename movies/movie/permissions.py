from rest_framework import permissions


class IsAdmin(permissions.BasePermission):  # permission that will return true if current user is admin
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)


class IsEditable(permissions.BasePermission):  # This will true for admin or user's get, option and head request
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            if request.method in permissions.SAFE_METHODS:  # This checks for get, option, head
                return True
            return False


class IsUser(permissions.BasePermission):  # This will check if current user is normal user or admin for review system
    def has_permission(self, request, view):
        if request.user.is_superuser:
            if request.method in permissions.SAFE_METHODS:
                return True
            return False
        else:
            return True


