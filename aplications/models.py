# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from api_rest.models import DatedModel


class AplicationsModel(DatedModel):
    server = models.ForeignKey(
        'servers.ServersModel',
        verbose_name=_(u'servidores'),
        related_name=u'aplications'
    )
    aplication = models.CharField(
        _(u'aplicação'),
        max_length=255
    )

    def __unicode__(self):
        return u'%s' % (self.aplication)
