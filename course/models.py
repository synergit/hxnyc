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


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=250, blank=False, verbose_name="teacher name")
    teacher_email = models.CharField(max_length=250, blank=False, verbose_name="teacher email")
    creator = models.ForeignKey(User, verbose_name="creator", null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name="created date", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="modified data", default=datetime.now)

class Registration(models.Model):
    student_name = models.CharField(max_length=135, verbose_name="student name")
    contact_name = models.ForeignKey(User, verbose_name="contact_name", null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=135, verbose_name="address")
    phone = models.CharField(max_length=135,  verbose_name="phone")
    email = models.EmailField(max_length=135, blank=True, verbose_name="email")
    registered_class = models.CharField(max_length=135, blank=True, verbose_name="registered class")
    created_date = models.DateTimeField(verbose_name="created date", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="modified data", default=datetime.now)

    class Meta:
        verbose_name = "Registration"
        verbose_name_plural = "Registrations"