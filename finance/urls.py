from django.conf.urls import url
from django.views.generic import ListView, DetailView
from finance.models import Providers

urlpatterns = [
    url(r'^', ListView.as_view(queryset=Providers.objects.all().order_by('-id'), template_name='finance/info.html'))
]