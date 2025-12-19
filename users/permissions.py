from rest_framework.permissions import BasePermission
from django.db import models


class IsAdmin(BaseException):
    def has_permission(self, request, view):
        return request.user.role['admin']
    
class IsClient(BaseException):
    def has_permission(self, request, view):
        return request.user.role['client']

class WalletIsLocked(BasePermission):
    def has_object_permission(self, request, view):
        return request.user.client.wallet.is_locked
