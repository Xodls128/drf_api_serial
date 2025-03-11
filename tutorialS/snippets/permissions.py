from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

class IsOwnerOrReadOnLy(permissions.BasePermission):
    '''
    커스텀 펄미션: 오너만 수정할수 있게함
    '''
    def has_object_permission(self, request, view, obj):
        #읽기는 모두 가능
        #GET, HEAD, OPTIONS 요청은 항상 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        #쓰기는 오너만 가능
        return obj.owner == request.user
    
permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]