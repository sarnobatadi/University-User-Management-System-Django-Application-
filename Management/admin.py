from django.contrib import admin
from Management.models import Section,Student,StudentSection,Course,CourseInstructor,Instructor,Department
# Register your models here.
admin.site.register(Section)
admin.site.register(Instructor)
admin.site.register(Department)
admin.site.register(StudentSection)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseInstructor)