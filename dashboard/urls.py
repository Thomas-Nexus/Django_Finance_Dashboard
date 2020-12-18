from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spy/', spy, name='spy'),
    path('dax/', dax, name='dax'),
    path('btc/', btc, name='btc'),
    path('gold/', gold, name='gold'),
    path('oil/', oil, name='oil'),
    path('dxy/', dxy, name='dxy'),
    path('tlt/', tlt, name='tlt'),

    path('spy30/', spy30, name='spy30'),
    path('dax30/', dax30, name='dax30'),
    path('btc30/', btc30, name='btc30'),
    path('gold30/', gold30, name='gold30'),
    path('dxy30/', dxy30, name='dxy30'),
    path('oil30/', oil30, name='oil30'),
    path('tlt30/', tlt30, name='tlt30'),
]