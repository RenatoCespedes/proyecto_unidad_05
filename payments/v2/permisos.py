from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # if request.user.is_authenticated and request.method in ['get']:
        #     return True
        if request.user.is_authenticated and view.action=='list':
            return True
        elif request.user.is_superuser:
            return True
        return False

class UserPaymentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (view.action in ['list','retrieve','create']):
            return True
        elif request.user.is_superuser:
            return True
        return False

class UserExpiredPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (view.action in ['list','retrieve']):
            return True
        elif request.user.is_superuser:
            return True
        return False
