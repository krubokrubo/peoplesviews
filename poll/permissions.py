# Taken from Django Rest Framework tutorial
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # always allow "safe" (read-only) GET, HEAD or OPTION requests
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
