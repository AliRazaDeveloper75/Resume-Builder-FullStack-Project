from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def protected_view(request):
    return Response({
        'message': 'This is a protected view!',
        'user': request.user.username
    })

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def public_view(request):
    return Response({
        'message': 'This is a public view!'
    })