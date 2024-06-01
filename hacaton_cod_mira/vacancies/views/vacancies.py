from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import parsers
from rest_framework.response import Response
from rest_framework import status
import json

from vacancies.serializers.vacancies_serializer import (VacancySerializer, VacanciesCreteSerializer, 
                                                        VacanciesUpdateSerializer)
from hacaton_cod_mira.swagger_service.apply_swagger_auto_schema import apply_swagger_auto_schema
from vacancies.models.vacancy import Vacancy


class VacanciesViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return VacanciesCreteSerializer
        elif self.action in ['update', 'partial_update']:
            return VacanciesUpdateSerializer
        return VacancySerializer

    def perform_create(self, serializer):
        user = self.request.user
        vacancy = serializer.save()
        vacancy.competention.set(serializer.validated_data['competention'])
        return vacancy

    def perform_update(self, serializer):
        user = self.request.user
        vacancy = serializer.save()
        vacancy.competention.set(serializer.validated_data['competention'])
        return vacancy

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, pk):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



VacanciesViewSet = apply_swagger_auto_schema(
    tags=['vacancies'], excluded_methods=[]
)(VacanciesViewSet)
