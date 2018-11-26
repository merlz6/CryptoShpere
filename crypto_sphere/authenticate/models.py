# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#extend user class for balanaces?
class fullUser(User):
        balanceBTC = models.IntegerField(default=0)
        balanceLTC = models.IntegerField(default=0)
        balanceXRP = models.IntegerField(default=0)
        balanceETH = models.IntegerField(default=0)
        balanceXLM = models.IntegerField(default=0)
        balanceXMR = models.IntegerField(default=0)
        balanceADA = models.IntegerField(default=0)
        balanceTRX = models.IntegerField(default=0)

class Meta:
        model = User
        fields = (    'balanceBTC',
            'balanceLTC',
            'balanceXRP',
            'balanceETH',
            'balanceXLM',
            'balanceXMR',
            'balanceADA',
            'balanceTRX',
            )
