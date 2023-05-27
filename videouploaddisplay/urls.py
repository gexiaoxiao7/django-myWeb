from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.upload_display_video, name='upload_display_video'),
    path('doCheck/', views.do_check, name='doCheck'),
    path('doResult/', views.do_result, name='doResult'),
    path('doAgain/', views.do_again, name='doAgain'),
]