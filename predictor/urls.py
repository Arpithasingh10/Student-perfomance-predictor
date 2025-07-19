from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_result, name='predict_result'),
]
