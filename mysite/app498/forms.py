# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import autocomplete_light.shortcuts as al
al.autodiscover()

from .models import History


class CreateHistoryForm(al.ModelForm):

    class Meta:
        model = History
        fields = ('start_date', 'code_text', )
