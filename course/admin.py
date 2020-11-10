from django.contrib import admin
from course.models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    list_display = ('course_name', 'course_type', 'course_desp', 'creator', 'created_date', 'modified_date')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Course, CourseAdmin)
