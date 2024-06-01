from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import parsers
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

from users.models.user import User
from users.serializers.users_serializer import UserSerializer
from hacaton_cod_mira.swagger_service.apply_swagger_auto_schema import apply_swagger_auto_schema


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    parser_classes = [parsers.JSONParser, ]
    serializer_class = UserSerializer

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return (
                User.objects.none()
            )
        user = self.request.user
        if self.action in ['list', ]:
            if user.is_superuser:
                return User.objects.exclude(is_superuser=True)
            if not User.objects.filter(role="Кандидат"):
                return User.objects.filter(role="Кандидат")
            if User.objects.filter(role="Кандидат"):
                return Response(
                    "Вы не можете просматривать пользователей.",
                    status=status.HTTP_403_FORBIDDEN
                )
        
        return None
    

UsersViewSet = apply_swagger_auto_schema(
    tags=['users'], excluded_methods=[]
)(UsersViewSet)