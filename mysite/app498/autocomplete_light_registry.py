# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import autocomplete_light.shortcuts as al
from .models import CodeText


al.register(CodeText,
    search_fields=['^code'],
    attrs={
        'placeholder': 'Start typing...',
        'data-autocomplete-minimum-characters': 1,
    },
    widget_attrs={
        'data-widget-maximum-values': 4,
        'class': 'modern-style',
    },
)
