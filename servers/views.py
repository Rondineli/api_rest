from django.shortcuts import get_object_or_404
from rest_framework import generics

from servers.models import ServersModel
from rest_framework import (
    serializers,
    viewsets
)


class ServersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServersModel
        fields = ('server_name', 'ip', 'is_active')


class ServersViewSet(viewsets.ModelViewSet):
    queryset = ServersModel.objects.all()
    serializer_class = ServersSerializer
