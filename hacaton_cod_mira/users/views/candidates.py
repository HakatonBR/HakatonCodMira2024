from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import parsers
from rest_framework.response import Response
from rest_framework import status
import json

from hacaton_cod_mira.swagger_service.apply_swagger_auto_schema import apply_swagger_auto_schema
from users.serializers.candidates import CandidateSerializer, CandidateCreateSerializer, CandidateUpdateSerializer
from users.models.candidate import Candidate


class CandidatesViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CandidateCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return CandidateUpdateSerializer
        return CandidateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

