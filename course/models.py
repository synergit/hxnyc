from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# from django_prometheus.models import ExportModelOperationsMixin
from django.utils.translation import gettext_lazy as _

CourseTypes = [
    (0, "chinese"),
    (1, "culture"),
    (2, "adult")
]


#
#  Create your models here.
class Course(models.Model):
    # Translator: Course
    course_type = models.SmallIntegerField(blank=False, choices=CourseTypes, verbose_name=_("course type"))
    course_name = models.CharField(max_length=250, blank=False, verbose_name=_("course name"))
    course_desp = models.TextField(max_length=250, blank=True, verbose_name=_("course description"))
    creator = models.ForeignKey(User, verbose_name=_("creator"), null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name=_("created date"), default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=_("modified data"), default=datetime.now)


class Teacher(models.Model):
    # Translator: Teacher
    teacher_name = models.CharField(max_length=250, blank=False, verbose_name=_("teacher name"))
    teacher_email = models.CharField(max_length=250, blank=False, verbose_name=_("teacher email"))
    creator = models.ForeignKey(User, verbose_name=_("creator"), null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name=_("created date"), default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=_("modified data"), default=datetime.now)

# class Registration(ExportModelOperationsMixin('Registration'), models.Model):
class Registration(models.Model):
    # Translator: Registration
    student_name = models.CharField(max_length=135, verbose_name=_("student name"))
    contact_name = models.ForeignKey(User, verbose_name=_("contact_name"), null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=135, verbose_name=_("address"))
    phone = models.CharField(max_length=135,  verbose_name=_("phone"))
    email = models.EmailField(max_length=135, blank=True, verbose_name=_("email"))
    registered_class = models.CharField(max_length=135, blank=True, verbose_name=_("registered class"))
    created_date = models.DateTimeField(verbose_name=_("created date"), default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=_("modified data"), default=datetime.now)

    class Meta:
        verbose_name = _("Registration")
        verbose_name_plural = _("Registrations")