from django.contrib import admin

# Register your models here.
from enrollment.models import StudentExt

class StudentAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    list_display = ('student_name', 'contact_name', 'enrolled_course')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

# Register your models here.
admin.site.register(StudentExt, StudentAdmin)