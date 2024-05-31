from django.contrib.auth import logout
from django.http import HttpResponse
from rest_framework import permissions, serializers
from rest_framework import generics

from hacaton_cod_mira.swagger_service.apply_swagger_auto_schema import apply_swagger_auto_schema


class EmptySerializer(serializers.Serializer):
    """
    КОСТЫЛЬ, пока не трогать!!!!!!!!!!!!!!!
    """
    pass


class LogoutView(generics.GenericAPIView):
    """<h2>/api/users/logout/</h2>\n"""

    permission_classes = [permissions.AllowAny]
    serializer_class = EmptySerializer

    def post(self, request):
        logout(request)
        response = HttpResponse(status=200)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response


LogoutView = apply_swagger_auto_schema(
    tags=["login / logout / register"], excluded_methods=[]
)(LogoutView)