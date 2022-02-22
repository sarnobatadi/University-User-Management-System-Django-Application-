from statistics import mode
from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=20,primary_key=True)
    building = models.CharField(max_length=40, null=True)
    budget = models.IntegerField(null=True)
    def __str__(self):
        return self.dept_name

class Course(models.Model):
    course_id = models.CharField(primary_key=True,max_length=10)
    title = models.CharField(max_length=50, null=True)
    dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    credits = models.IntegerField(null=True)
    def __str__(self):
        return self.course_id

class TimeSlot(models.Model):
    timeslot_id = models.CharField(primary_key=True,max_length=10)
    day = models.CharField(null=True,max_length=20)
    start_time = models.CharField(null=True,max_length=20)
    end_time = models.CharField(null=True,max_length=20)
    def __str__(self):
        return self.timeslot_id 

class Classroom(models.Model):
    room_no = models.CharField(primary_key=True,max_length=10)
    class_buiding = models.CharField(max_length=25,null=True)
    capacity = models.IntegerField(null=True)
    def __str__(self):
        return self.room_no


class Section(models.Model):
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    sec_id = models.CharField(primary_key=True,max_length=10)
    semester = models.CharField(max_length=10 ,null=True)
    year = models.CharField(max_length=10,null=True)
    section_buidling = models.CharField(max_length=40,null=True)
    room_no = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    timeslot_id = models.ForeignKey(TimeSlot,on_delete=models.CASCADE)
    def __str__(self):
        return self.sec_id


class Student(models.Model):
    stud_id = models.CharField(primary_key=True,max_length=10)
    stud_name = models.CharField(max_length=50)
    dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    tot_cred = models.IntegerField(null=True)
    def __str__(self):
        return self.stud_id

class StudentSection(models.Model):
    stud_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    sec_id = models.ForeignKey(Section,on_delete=models.CASCADE)
    semester = models.CharField(max_length=10,null=True)
    year = models.CharField(max_length=10,null=True)
    grade = models.CharField(max_length=6,null=True)
    

class Instructor(models.Model):
    instrustor_id = models.CharField(primary_key=True,max_length=10)
    instrustor_name = models.CharField(max_length=50,null=True)
    dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField(null=True)
    def __str__(self):
        return self.instrustor_id

class CourseInstructor(models.Model):
    instructor_id = models.ForeignKey(Instructor,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    sec_id = models.ForeignKey(Section,on_delete=models.CASCADE)
    semester = models.CharField(max_length=10,null=True)
    year = models.CharField(max_length=10,null=True)

class Prereq(models.Model):
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    prereq_id = models.CharField(max_length=10,null=True)

class Advisor(models.Model):
    s_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    i_id = models.ForeignKey(Instructor,on_delete=models.CASCADE)