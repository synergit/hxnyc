from django.contrib import admin
from course.models import Course, Teacher, Registration
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    list_display = ('course_name', 'course_type', 'course_desp')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

class TeacherAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    list_display = ('teacher_name', 'teacher_email')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

class RegistrationAdmin(admin.ModelAdmin):
    # exclude = ('creator','created_date','modified_date')
    list_display = ('student_name', 'contact_name', 'registered_class')
    
    readonly_fields = ('contact_name', 'created_date','modified_date')

    fieldsets = (
        (None, {'fields': (
            "contact_name", ("student_name", "address", "phone", "email"),
            ('created_date', 'modified_date'),
            "registered_class", )}),
    )
    def save_model(self, request, obj, form, change):
        obj.contact_name = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Registration, RegistrationAdmin)
