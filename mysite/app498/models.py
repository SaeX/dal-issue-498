# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class CodeText(models.Model):
    code = models.CharField(max_length=30, blank=True)
    text = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return u"%s (%s)" % (self.code, self.text)


@python_2_unicode_compatible
class History(models.Model):
    code_text = models.ForeignKey(CodeText)
    start_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return "%s: %s" % (self.start_date, self.code_text.code)
