from django.conf.urls import url
from django.urls import path

from course import views


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^course/(?P<course_id>\d+)/$', views.detail, name='detail'),
    path('register/add/', views.RegisterCreateView.as_view(), name='resume-add'),
]