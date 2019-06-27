from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView

class ArticleListView(TemplateView):
    template_name = 'article_list.html'
