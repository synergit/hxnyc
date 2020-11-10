from django.conf.urls import url

from course import views


urlpatterns = [
    url(r"^courselist/", views.courselist, name="courselist"),
    url(r'^course/(?P<course_id>\d+)/$', views.detail, name='detail'),
]