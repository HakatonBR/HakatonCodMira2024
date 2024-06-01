from rest_framework import serializers
from users.models import Candidate, CareerProfile, CompetentionProfile


class CompetentionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetentionProfile
        fields = '__all__'


class CareerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerProfile
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    competention_profile = CompetentionProfileSerializer()
    career_profile = CareerProfileSerializer()

    class Meta:
        model = Candidate
        fields = (
            'candidate_id', 
            'last_name',
            'first_name', 
            'surname',
            'resume_link',
            'competention_profile',
            'career_profile',
            'sex',
            'age',
            'army_status',
            'education',
            'languages',
            'status',
            'comments',
            'user',
            'vacancy',
            'phone_number'
        )


class CandidateCreateSerializer(serializers.ModelSerializer):
    competention_profile = CompetentionProfileSerializer()
    career_profile = CareerProfileSerializer()

    class Meta:
        model = Candidate
        fields = (
            'last_name',
            'first_name', 
            'surname',
            'resume_link',
            'competention_profile',
            'career_profile',
            'sex',
            'age',
            'army_status',
            'education',
            'languages',
            'status',
            'comments',
            'user',
            'vacancy',
            'phone_number'
        )

    def create(self, validated_data):
        competention_profile_data = validated_data.pop('competention_profile')
        career_profile_data = validated_data.pop('career_profile')

        competention_profile = CompetentionProfile.objects.create(**competention_profile_data)
        career_profile = CareerProfile.objects.create(**career_profile_data)

        candidate = Candidate.objects.create(
            competention_profile=competention_profile,
            career_profile=career_profile,
            **validated_data
        )

        return candidate


class CandidateUpdateSerializer(serializers.ModelSerializer):
    competention_profile = CompetentionProfileSerializer()
    career_profile = CareerProfileSerializer()

    class Meta:
        model = Candidate
        fields = (
            'candidate_id',
            'last_name',
            'first_name', 
            'surname',
            'resume_link',
            'competention_profile',
            'career_profile',
            'sex',
            'age',
            'army_status',
            'education',
            'languages',
            'status',
            'comments',
            'user',
            'vacancy',
            'phone_number'
        )

    def update(self, instance, validated_data):
        competention_profile_data = validated_data.pop('competention_profile')
        career_profile_data = validated_data.pop('career_profile')

        # Update CompetentionProfile
        competention_profile = instance.competention_profile
        competention_profile.scorepoint_hard_skill = competention_profile_data.get('scorepoint_hard_skill', competention_profile.scorepoint_hard_skill)
        competention_profile.scorepoint_soft_skill = competention_profile_data.get('scorepoint_soft_skill', competention_profile.scorepoint_soft_skill)
        competention_profile.scorepoint_job_vacancy = competention_profile_data.get('scorepoint_job_vacancy', competention_profile.scorepoint_job_vacancy)
        competention_profile.competention = competention_profile_data.get('competention', competention_profile.competention)
        competention_profile.save()

        # Update CareerProfile
        career_profile = instance.career_profile
        for attr, value in career_profile_data.items():
            setattr(career_profile, attr, value)
        career_profile.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance
