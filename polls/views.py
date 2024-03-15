from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import agendaPersonal


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return agendaPersonal.objects.order_by('id')[:5]


class DetailView(generic.DetailView):
    model = agendaPersonal
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = agendaPersonal
    template_name = 'polls/results.html'


def vote(request, question_id):
    ...