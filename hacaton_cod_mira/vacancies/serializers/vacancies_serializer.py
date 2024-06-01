from rest_framework import serializers
from vacancies.models import Vacancy
from users.models.competention import Competention

class VacanciesCreteSerializer(serializers.Serializer):
    vacancy_name = serializers.CharField(max_length=125, help_text="Название вакансии")
    vacancy_text = serializers.CharField(help_text="Описание вакансии")
    competention = serializers.ListField()

    def validate(self, attrs):
        if not all([attrs.get('vacancy_name'), attrs.get('vacancy_text')]):
            raise serializers.ValidationError("Все поля обязательны.")
        
        return attrs

class VacancySerializer(serializers.ModelSerializer):
    competention = serializers.SerializerMethodField()

    class Meta:
        model = Vacancy
        fields = ('vacancy_id', 'vacancy_name', 'vacancy_text', 'competention')

    def get_competention(self, obj):
        return [{
            'competention_id': c.competention_id,
            'competention_name': c.competention_name
        } for c in obj.competention.all()]


class VacanciesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('vacancy_id', 'vacancy_name', 'vacancy_text', 'competention')

