from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Student(models.Model):
    student_name = models.CharField(max_length=135, verbose_name='student name')
    contact_name = models.CharField(max_length=135, verbose_name='contact name')
    address = models.CharField(max_length=135, verbose_name='address')
    phone = models.CharField(max_length=135, verbose_name='phone')
    email = models.EmailField(max_length=135, verbose_name='email')
    enrolled_course = models.CharField(max_length=135, verbose_name='enrolled course')
    student_dob = models.CharField(max_length=135, verbose_name='student DOB')
    creator = models.ForeignKey(User, verbose_name="creator", null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name="created date", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="modified data", default=datetime.now)
    # last_editor = models.CharField(max_length=256, blank=True, verbose_name='last editor')


    class Meta:
        db_table = 'student'
        verbose_name = 'student'
        verbose_name_plural = 'students'

        permissions = [
            ("export", "Can export student list"),
            # ("notify", "notify interviewer for student review"),
        ]
    def __unicode__(self):
        return self.student_name


    def __str__(self):
        return self.student_name