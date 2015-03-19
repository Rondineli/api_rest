from rest_framework import generics

from aplications.models import AplicationsModel
from rest_framework import (
    serializers,
    viewsets
)


class AplicationsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AplicationsModel
        fields = ('aplication', 'server')


class AplicationsViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = AplicationsModel.objects.all()
    serializer_class = AplicationsSerializer
    lookup_field = 'aplication'
