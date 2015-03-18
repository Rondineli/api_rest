from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User

from django.contrib import admin

from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

"""
# Examples:
# url(r'^$', 'api_rest.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
"""
urlpatterns = patterns(
    '',
    url(
        r'^',
        include(
            router.urls
        )
    ),
    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    url(
        r'^admin/',
        include(
            admin.site.urls
        )
    ),
)
