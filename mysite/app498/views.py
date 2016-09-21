# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.core.urlresolvers import reverse

from .models import History
from .forms import CreateHistoryForm


class ListHistoryView(generic.ListView):

    template_name = 'list.html'
    model = History


class CreateHistoryView(generic.CreateView):

    template_name = 'add.html'
    model = History
    form_class = CreateHistoryForm

    def get_success_url(self):
        return reverse('list')
