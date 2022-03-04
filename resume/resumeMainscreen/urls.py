from django.urls import path, include
from . import views

urlpatterns = [
    path('<lang>', views.main, name = 'images'),
]