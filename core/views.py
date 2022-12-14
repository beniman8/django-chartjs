from django.shortcuts import render
from .models import Club
from django.views.generic import TemplateView



class ClubChartView(TemplateView):

    template_name='chart.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['qs'] = Club.objects.all()

        return context
