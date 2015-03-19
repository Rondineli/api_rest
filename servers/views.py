from rest_framework import generics

from servers.models import ServersModel
from rest_framework import (
    serializers,
    viewsets
)


class ServersSerializer(serializers.HyperlinkedModelSerializer,
                        serializers.ModelSerializer):
    aplications = serializers.StringRelatedField(many=True)

    class Meta:
        model = ServersModel
        fields = ('server_name', 'ip', 'is_active', 'aplications', 'pk')


class ServersViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = ServersModel.objects.filter(is_active=True)
    serializer_class = ServersSerializer
