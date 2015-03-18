# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from api_rest.models import DatedModel


class ServersModel(DatedModel):
    server_name = models.CharField(
        _(u'nome do servidor'),
        max_length=255,
        db_index=True
    )
    is_active = models.BooleanField(
        _(u'está ativo?'),
        default=True
    )
    ip = models.CharField(
        _(u'ip do servidor'),
        max_length=40
    )

    def __unicode__(self):
        return unicode(self.server_name)
