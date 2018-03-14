from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS

class GalleryGroupPermissions(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return request.user.has_perms('gallery.delete_group')
        elif request.method in ('POST', 'PUT', 'PATCH'):
            return obj.can_edit(request.user)

        return False

class GalleryGroupMembershipPermissions(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            # Anyone can join a group
            return True
        elif request.method == 'DELETE':
            # Anyone can leave a group and group admins can remove anyone
            return obj.user_id == request.user.id or obj.group.can_edit(request.user)
        
        elif request.method in ('PUT', 'PATCH'):
            # Only group admins can modify memberships
            return obj.group.can_edit(request.user)
        
        elif request.method in SAFE_METHODS:
            # Membership lists are public
            return True
        
        return False

class GallerySubmissionPermissions(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.can_edit(request.user)
