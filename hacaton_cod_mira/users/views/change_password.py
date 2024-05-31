from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password

from users.serializers.change_password_serializer import ChangePasswordSerializer
from hacaton_cod_mira.swagger_service.apply_swagger_auto_schema import apply_swagger_auto_schema


class ChangePasswordAPIView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    parser_classes = [MultiPartParser, ]

    def put(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        if not check_password(serializer.validated_data.get('old_password'), user.password):
            return Response(
                "Старые пароли не совпадают.",
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.set_password(serializer.validated_data.get('new_password'))
        user.save()

        return Response(
            "Your password has been updated.",
            status=status.HTTP_200_OK
        )


ChangePasswordAPIView = apply_swagger_auto_schema(
    tags=['change password'], excluded_methods=[]
)(ChangePasswordAPIView)
