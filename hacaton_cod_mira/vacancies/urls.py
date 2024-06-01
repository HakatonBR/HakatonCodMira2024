from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vacancies.views.vacancies import VacanciesViewSet

router = DefaultRouter()
router.register(r'vacancies', VacanciesViewSet, basename='vacancy')

urlpatterns = [
    path('', include(router.urls)),
]