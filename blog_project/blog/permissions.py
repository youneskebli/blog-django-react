from rest_framework.permissions import BasePermission


class IsEditor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.writer.is_editor


class IsWriterOrEditor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.writer.is_editor:
            return True
        return obj.written_by == request.user
