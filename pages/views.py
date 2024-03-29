from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Content
from sentiment_analysis import analyze_text
import os
from django.conf.global_settings import STATIC_ROOT


class IndexPageView(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        form = Content()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = Content(request.POST)
        if form.is_valid():
            text = request.POST['text']
            label, score, magnitude, short_text = analyze_text(text)
            context = {
                'label': label,
                'score': score,
                'magnitude': magnitude,
                'short_text': short_text,
                'form': Content()}
            return render(request, self.template_name, context)
        return render(request, self.template_name, {'form': form})