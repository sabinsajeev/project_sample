from django.urls import path
from . import  views

urlpatterns=[
    path('',views.create_view),
    path('<id>',views.detail_view),
]