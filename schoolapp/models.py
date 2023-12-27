from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),
    )
    
    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
class Section(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
class Session_year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)
    
    def __str__(self):
        return self.session_start +" To "+ self.session_end
    
class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    dob = models.DateField(auto_now=False)
    gender = models.CharField(max_length=100)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    religion = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    address = models.TextField()
    section_id = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_id = models.ForeignKey(Session_year,on_delete=models.DO_NOTHING)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name + "  " + self.admin.last_name
    
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    address = models.TextField()
    create_date = models.DateField(auto_now_add=True,null=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.admin.username
class Subject(models.Model):
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True,null=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return  self.name
class Staff_notification(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)
    
    def __str__(self):
        return self.staff_id.admin.first_name + "  " + self.staff_id.admin.last_name
class Staff_leave(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    date_end = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
   
    
    def __str__(self):
        return self.staff_id.admin.first_name + " "+ self.staff_id.admin.last_name

    
    