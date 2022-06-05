from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="main/index.html")),
]
