from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

CourseTypes = [
    (0, "chinese"),
    (1, "culture"),
    (2, "adult")
]


#
#  Create your models here.
class Course(models.Model):
    course_type = models.SmallIntegerField(blank=False, choices=CourseTypes, verbose_name="course type")
    course_name = models.CharField(max_length=250, blank=False, verbose_name="course name")
    course_desp = models.TextField(max_length=250, blank=True, verbose_name="course description")
    creator = models.ForeignKey(User, verbose_name="creator", null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name="created date", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="modified data", default=datetime.now)
