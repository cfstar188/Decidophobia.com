from rest_framework import permissions

class ProductPermissions(permissions.BasePermission):
    AdminKey = 'decidophobiaAdmin'

    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True
        if request.method == 'GET':
            return False
        else:
            return request.headers.get('Key', '') == self.AdminKey
