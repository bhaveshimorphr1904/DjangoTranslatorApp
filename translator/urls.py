from . import views
from django.urls import path

urlpatterns = [
    # From dose not need .as_view()
    path('', views.translator_view, name='translator_view')
]
