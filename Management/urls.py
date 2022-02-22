from django.contrib import admin
from django.urls import path
from Management import views
urlpatterns = [
    path('', views.getStudentdata),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('Course/', views.getCoursedata),
    path('Student/', views.getStudentdata),
    path('Faculty/', views.getFacultydata),
    path('Department/', views.getDepartmentdata),
    path('TimeSlot/', views.getTimeSlotData),
    path('Section/', views.getSectiondata),
    path('Classroom/', views.getClassroomData),
    path('StudentCourse/', views.getStudentTakesdata),
    path('FacultyCourse/', views.getFacultyTeachesdata),
    path('Advisor/', views.getAdvisordata),
    path('Prereq/',views.getPrereqdata),
    path('deleteStudentTakes/<str:id>', views.deleteStudentCourse),
    path('deleteStudent/<str:id>', views.deleteStudentData),
    path('deleteFaculty/<str:id>', views.deleteFacultyData),
    path('deleteDepartment/<str:id>', views.deleteDepartmentData),
    path('deleteCourse/<str:id>', views.deleteCourseData),
    path('deleteFacultyTeaches/<str:id>', views.deleteFacultyCourse),
    path('deleteSection/<str:id>', views.deleteSection),
    path('deleteClassroom/<str:id>', views.deleteClassroom),
    path('deleteTimeslot/<str:id>', views.deleteTimeslot),
    path('deleteAdvisor/<str:id>', views.deleteAdvisor),
    path('deletePrereq/<str:id>',views.deletePrereq),



]
