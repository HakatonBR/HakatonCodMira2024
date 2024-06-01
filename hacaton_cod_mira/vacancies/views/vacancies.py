from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import parsers
from rest_framework.response import Response
from rest_framework import status
import json

from vacancies.serializers.vacancies_serializer import VacancySerializer, VacanciesCreteSerializer
from hacaton_cod_mira.swagger_service.apply_swagger_auto_schema import apply_swagger_auto_schema
from vacancies.models.vacancy import Vacancy


class VacanciesViewSet(viewsets.ViewSet):
    parser_classes = [parsers.JSONParser, ]

    def list(self, request):
        queryset = Vacancy.objects.all()
        serializer = VacancySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        user = request.user

        serializer = VacanciesCreteSerializer(data=request.data)
        serializer.is_valid()

        if user:
            vacancy = Vacancy.objects.create(
                vacancy_name=serializer.data['vacancy_name'],
                vacancy_text=serializer.data['vacancy_text']
            )

            vacancy.competention.set(serializer.data['competention'])

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


VacanciesViewSet = apply_swagger_auto_schema(
    tags=['vacancies'], excluded_methods=[]
)(VacanciesViewSet)
