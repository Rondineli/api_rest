from rest_framework import generics

from servers.models import ServersModel
from rest_framework import (
    serializers,
    viewsets,
    filters
)


class ServersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServersModel
        fields = ('server_name', 'ip', 'is_active')


class ServersViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = ServersModel.objects.filter(is_active=True)
    serializer_class = ServersSerializer
    lookup_field = 'server_name'
