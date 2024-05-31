from django.urls import path
from .views import register1,register2
app_name='app1'

urlpatterns = [
    path('register1/',register1,name='register1'),
    path('register2/',register2,name='register2'),
]
