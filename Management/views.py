from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from Management.models import Advisor, Classroom, Course, CourseInstructor,Department, Prereq, Section, Student,Instructor, StudentSection, TimeSlot
# Create your views here.

def home(request):
    return render(request,'Login/landingPage.html')


def getAdvisordata(request):

    if request.method == 'POST':
        newrecord = Advisor()
        newrecord.s_id = Student.objects.get(stud_id =request.POST.get('s_id'))
        newrecord.i_id = Instructor.objects.get(instrustor_id = request.POST.get('i_id'))
        newrecord.save()

    courses = Advisor.objects.all().order_by('s_id')
    options1 = Student.objects.filter(~Q(stud_id =''))
    options2 = Instructor.objects.filter(~Q(instrustor_id =''))
    data = {
        'FormData':courses,
        'OptionData1':options1,
        'OptionData2':options2
    }
    return render(request,'Forms/form_advisor.html',data)


def getPrereqdata(request):

    if request.method == 'POST':
        newrecord = Prereq()
        newrecord.course_id = Course.objects.get(course_id =request.POST.get('course_id'))
        newrecord.prereq_id = Course.objects.get(course_id =request.POST.get('prereq_id'))
        newrecord.save()

    courses = Prereq.objects.all().order_by('prereq_id')
    options1 = Course.objects.filter(~Q(course_id =''))
    options2 = Course.objects.filter(~Q(course_id =''))
    data = {
        'FormData':courses,
        'OptionData1':options1,
         'OptionData2':options2,
       
    }
    return render(request,'Forms/form_prereq.html',data)

def getCoursedata(request):

    if request.method == 'POST':
        newrecord = Course()
        print(request.POST.get('dept_name'))
        dept = Department.objects.filter(dept_name = request.POST.get('dept_name') )
        print(dept)
        newrecord.dept_name = Department.objects.get(dept_name =request.POST.get('dept_name'))
        newrecord.credits = request.POST.get('credits')
        newrecord.course_id = request.POST.get('course_id')
        newrecord.title = request.POST.get('title')
        newrecord.save()

    courses = Course.objects.all().order_by('course_id')
    options = Department.objects.filter(~Q(dept_name =''))
    print(options)
    data = {
        'FormData':courses,
        'OptionData':options
    }
    return render(request,'Forms/form_course.html',data)

def getStudentdata(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newrecord = Student()
            print(request.POST.get('dept_name'))
            dept = Department.objects.filter(dept_name = request.POST.get('dept_name') )
            print(dept)
            newrecord.dept_name = Department.objects.get(dept_name =request.POST.get('dept_name'))
            newrecord.tot_cred = request.POST.get('tot_cred')
            newrecord.stud_name = request.POST.get('stud_name')
            newrecord.stud_id = request.POST.get('stud_id')
            newrecord.save()

        courses = Student.objects.all().order_by('stud_id')
        options = Department.objects.filter(~Q(dept_name =''))
        print(options)
        data = {
            'FormData':courses,
            'OptionData':options
        }
        return render(request,'Forms/form_student.html',data)
    else:
        return render(request,'registration/login.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/Student/')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'registration/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')

def getFacultydata(request):

    if request.method == 'POST':
        newrecord = Instructor()
        print(request.POST.get('dept_name'))
        dept = Department.objects.filter(dept_name = request.POST.get('dept_name') )
        print(dept)
        newrecord.dept_name = Department.objects.get(dept_name =request.POST.get('dept_name'))
        newrecord.salary = request.POST.get('salary')
        newrecord.instrustor_name = request.POST.get('instrustor_name')
        newrecord.instrustor_id = request.POST.get('instrustor_id')
        newrecord.save()

    courses = Instructor.objects.all().order_by('instrustor_id')
    options = Department.objects.filter(~Q(dept_name =''))
    print(options)
    data = {
        'FormData':courses,
        'OptionData':options
    }
    return render(request,'Forms/form_faculty.html',data)


def getSectiondata(request):

    if request.method == 'POST':
        newrecord = Section()
        newrecord.course_id = Course.objects.get(course_id = request.POST.get('course_id'))
        newrecord.timeslot_id = TimeSlot.objects.get(timeslot_id = request.POST.get('timeslot_id'))
        newrecord.room_no = Classroom.objects.get(room_no = request.POST.get('room_no'))
        newrecord.sec_id = request.POST.get('sec_id')
        newrecord.section_buidling = request.POST.get('section_buidling')
        newrecord.semester = request.POST.get('semester')
        newrecord.year = request.POST.get('year')
        newrecord.save()

    courses = Section.objects.all().order_by('sec_id')
    options1 = Course.objects.filter(~Q(course_id =''))
    options2 = Classroom.objects.filter(~Q(room_no =''))
    options3 = TimeSlot.objects.filter(~Q(timeslot_id =''))
    print(options1)
    data = {
        'FormData':courses,
        'OptionData1':options1,
        'OptionData2':options2,
        'OptionData3':options3,

    }
    return render(request,'Forms/form_section.html',data)


def getStudentTakesdata(request):

    if request.method == 'POST':
        newrecord = StudentSection()
        newrecord.stud_id = Student.objects.get(stud_id=request.POST.get('stud_id'))
        newrecord.course_id = Course.objects.get(course_id = request.POST.get('course_id'))
        newrecord.sec_id = Section.objects.get(sec_id = request.POST.get('sec_id'))
        newrecord.grade = request.POST.get('grade')
        newrecord.semester = request.POST.get('semester')
        newrecord.year = request.POST.get('year')
        newrecord.save()

    courses = StudentSection.objects.all().order_by('stud_id')
    options2 = Course.objects.filter(~Q(course_id =''))
    options1 = Student.objects.filter(~Q(stud_id =''))
    options3 = Section.objects.filter(~Q(sec_id =''))
    print(options1)
    data = {
        'FormData':courses,
        'OptionData1':options1,
        'OptionData2':options2,
        'OptionData3':options3,

    }
    return render(request,'Forms/form_studenttakes.html',data)


def getFacultyTeachesdata(request):

    if request.method == 'POST':
        newrecord = CourseInstructor()
        newrecord.instructor_id = Instructor.objects.get(instrustor_id=request.POST.get('instrustor_id'))
        newrecord.course_id = Course.objects.get(course_id = request.POST.get('course_id'))
        newrecord.sec_id = Section.objects.get(sec_id = request.POST.get('sec_id'))
        newrecord.semester = request.POST.get('semester')
        newrecord.year = request.POST.get('year')
        newrecord.save()

    courses = CourseInstructor.objects.all().order_by('instructor_id')
    options2 = Course.objects.filter(~Q(course_id =''))
    options1 = Instructor.objects.filter(~Q(instrustor_id =''))
    options3 = Section.objects.filter(~Q(sec_id =''))
    print(options1)
    data = {
        'FormData':courses,
        'OptionData1':options1,
        'OptionData2':options2,
        'OptionData3':options3,

    }
    return render(request,'Forms/form_facultyteaches.html',data)


def getDepartmentdata(request):

    if request.method == 'POST':
        newrecord = Department()
        print(request.POST.get('dept_name'))
        dept = Department.objects.filter(dept_name = request.POST.get('dept_name') )
        print(dept)
        newrecord.dept_name = request.POST.get('dept_name')
        newrecord.budget = request.POST.get('budget')
        newrecord.building = request.POST.get('building')
        newrecord.save()

    deptdata = Department.objects.filter(~Q(dept_name ='')).order_by('dept_name')
    
    data = {
        'FormData':deptdata,

    }
    return render(request,'Forms/form_department.html',data)


def getTimeSlotData(request):

    if request.method == 'POST':
        newrecord = TimeSlot()
       
        newrecord.timeslot_id = request.POST.get('timeslot_id')
        newrecord.day = request.POST.get('day')
        newrecord.start_time = request.POST.get('start_time')
        newrecord.end_time = request.POST.get('end_time')
        newrecord.save()

    timeSlotdata = TimeSlot.objects.all().order_by('timeslot_id')
    
    data = {
        'FormData':timeSlotdata,

    }
    return render(request,'Forms/form_timeslot.html',data)


def getClassroomData(request):

    if request.method == 'POST':
        newrecord = Classroom()
       
        newrecord.room_no = request.POST.get('room_no')
        newrecord.class_buiding = request.POST.get('class_buiding')
        newrecord.capacity = request.POST.get('capacity')
        newrecord.save()

    classroomdata = Classroom.objects.all().order_by('room_no')
    
    data = {
        'FormData':classroomdata,

    }
    return render(request,'Forms/form_classroom.html',data)

def deleteStudentData(request,id):
    deleteRecord = Student.objects.filter(stud_id = id).delete()
    courses = Student.objects.all().order_by('stud_id')
    options = Department.objects.filter(~Q(dept_name =''))
    print(options)
    data = {
        'FormData':courses,
        'OptionData':options
    }
    return render(request,'Forms/form_student.html',data)

def deleteFacultyData(request,id):
    deleteRecord = Instructor.objects.filter(instrustor_id = id).delete()
    courses = Instructor.objects.all().order_by('instrustor_id')
    options = Department.objects.filter(~Q(dept_name =''))
    print(options)
    data = {
        'FormData':courses,
        'OptionData':options
    }
    return render(request,'Forms/form_faculty.html',data)

def deleteDepartmentData(request,id):
    deleteRecord = Department.objects.filter(dept_name = id).delete()
    deptdata = Department.objects.all().order_by('dept_name')
    
    data = {
        'FormData':deptdata,

    }
    return render(request,'Forms/form_department.html',data)

def deleteCourseData(request,id):
    deleteRecord = Course.objects.filter(course_id = id).delete()
    deptdata = Department.objects.all().order_by('dept_name')
    
    courses = Course.objects.all().order_by('course_id')
    options = Department.objects.filter(~Q(dept_name =''))
    print(options)
    data = {
        'FormData':courses,
        'OptionData':options
    }
    return render(request,'Forms/form_course.html',data)


def deleteStudentCourse(request,id):
    deleteRecord = StudentSection.objects.filter(stud_id = id).delete()
    return redirect('/StudentCourse')

def deleteFacultyCourse(request,id):
    deleteRecord = CourseInstructor.objects.filter(instructor_id = id).delete()
    return redirect('/FacultyCourse')


def deleteSection(request,id):
    deleteRecord = Section.objects.filter(sec_id = id).delete()
    return redirect('/Section')

def deleteTimeslot(request,id):
    deleteRecord = TimeSlot.objects.filter(timeslot_id = id).delete()
    return redirect('/Timeslot')


def deleteAdvisor(request,id):
    deleteRecord = Advisor.objects.filter(s_id = id).delete()
    return redirect('/Advisor')

def deleteClassroom(request,id):
    deleteRecord = Classroom.objects.filter(room_no = id).delete()
    return redirect('/Classroom')

def deletePrereq(request,id):
    deleteRecord = Prereq.objects.filter(prereq_id = id).delete()
    return redirect('/Prereq')


