# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import autocomplete_light.shortcuts as al
al.autodiscover()

from .models import History

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CreateHistoryForm(al.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateHistoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = History
        fields = ('start_date', 'code_text', )
