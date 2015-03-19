from django.conf.urls import patterns, include, url
from django.contrib import admin

from servers.views import ServersViewSet
from aplications.views import AplicationsViewSet

from rest_framework import routers

"""


# Routers provide an easy way of automatically determining the URL conf.
"""
router = routers.DefaultRouter()
router.register(r'servers', ServersViewSet)
router.register(r'aplications', AplicationsViewSet)
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
