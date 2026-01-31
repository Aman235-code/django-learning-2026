from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view, permission_classes # type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly # type: ignore

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        return Response({"message": "List of posts public"})
    elif request.method == 'POST':
        return Response({"message": f"{request.user.username} only auth users post data"})

