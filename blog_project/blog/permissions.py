from rest_framework.permissions import BasePermission

class IsWriter(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and hasattr(request.user, 'writer'))


class IsEditor(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'writer') and
            request.user.writer.is_editor
        )


class IsWriterOrEditor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'writer') and (
                request.user.writer == obj.written_by or
                request.user.writer.is_editor
            )
        )