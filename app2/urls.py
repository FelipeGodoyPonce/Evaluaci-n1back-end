from django.urls import path
from . import views

urlpatterns=[
    path("inicio_app2/",views.index_app2)
]