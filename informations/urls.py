from django.urls import path
from . import views


urlpatterns = [
    path('app/', views.ListCreateInformation.as_view(), name='ListCreat'),
    path('app/<pk>', views.RetrieveUpdateDestroyInformation.as_view(), name='RetrieveUpdateDestroy')
]