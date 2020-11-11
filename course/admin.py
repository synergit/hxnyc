from django.contrib import admin
from course.models import Course, Teacher
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    list_display = ('course_name', 'course_type', 'course_desp')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

class TeacherAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    list_display = ('teacher_name', 'teacher_email', 'creator')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
