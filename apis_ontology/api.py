from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import permissions

from apis_bibsonomy.models import Reference


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'
        depth = 1


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
