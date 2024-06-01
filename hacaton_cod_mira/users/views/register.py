from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import parsers
from django.contrib.auth import get_user_model
from rest_framework import generics

from hacaton_cod_mira.swagger_service.apply_swagger_auto_schema import apply_swagger_auto_schema
from users.serializers.register_serializer import RegisterSerializer


User = get_user_model()


class RegisterAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = RegisterSerializer
    parser_classes = (parsers.JSONParser,)

    def post(self, request):
        email = request.data.get("email")

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Регистрация прошла успешно."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


RegisterAPIView = apply_swagger_auto_schema(
    tags=["login / logout / register"], excluded_methods=[]
)(RegisterAPIView)
