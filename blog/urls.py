from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeList.as_view(), name='home_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view')
]
