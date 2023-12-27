from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from loan_demand.models import LoanDmand
from schoolapp.models import Course,Session_year,Section,CustomUser,Student,Staff,Subject,Staff_notification,Staff_leave
# Function for Home
@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    student_male = Student.objects.filter(gender='male').count()
    student_female = Student.objects.filter(gender='Female').count()
    student = Student.objects.all()
    course = Course.objects.all()
    context = {
        'student_count':student_count,
        'staff_count':staff_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_male':student_male,
        'student_female':student_female,
        'student':student,
        'course':course
    }
    return render(request,'HOD/home.html',context)
# Function for Student
@login_required(login_url='/')
def add_student(request):
    course = Course.objects.all()
    session_year = Session_year.objects.all()
    section = Section.objects.all()
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        religion = request.POST.get('religion')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        course_id = request.POST.get('course')
        section_id = request.POST.get('section')
        session_id = request.POST.get('session')
          
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"This email Already used")
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"This username Already used")
            return redirect('add_student')
        
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=3                
            )
            user.set_password(password)
            user.save()
            course = Course.objects.get(id = course_id)
            section = Section.objects.get(id = section_id)
            session_year = Session_year.objects.get(id = session_id)
            
            student = Student(
                admin = user,
                dob=dob,
                gender=gender,
                father_name=fname,
                mother_name=mname,
                religion=religion,
                mobile_no=phone,
                address=address,
                section_id=section,
                course_id=course,
                session_id=session_year,
                
            )
            student.save()
            messages.success(request,user.first_name + " " + user.last_name + " " + "are Successfuly Added")
            return redirect('add_student')
        

    context = {
        'course':course,
        'session_year':session_year,
        'section':section,
    }
    return render(request,'hod/add_student.html',context)

def view_student(request):
    student = Student.objects.all()
    context = {
        'student':student,
    }
    return render(request,'hod/view_student.html',context)

def edit_student(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_year.objects.all()
    section = Section.objects.all()
    
    context = {
        'student':student,
        'course':course,
        'session_year':session_year,
        'section':section
    }
    return render(request, 'hod/edit_student.html',context)

def update_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        religion = request.POST.get('religion')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        course_id = request.POST.get('course')
        section_id = request.POST.get('section')
        session_id = request.POST.get('session')
        
        user = CustomUser.objects.get(id=student_id)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username  
        if password !=None and password !="":
            user.set_password(password)
        if profile_pic !=None and profile_pic !="":
            user.profile_pic = profile_pic
            
        user.save()
        
        student = Student.objects.get(admin = student_id)
        student.dob=dob
        student.gender=gender
        student.father_name=fname
        student.mother_name=mname
        student.religion=religion
        student.mobile_no=phone
        student.address=address
        
        course = Course.objects.get(id = course_id)
        student.course_id = course
        section = Section.objects.get(id = section_id)
        student.section_id = section
        session_year = Session_year.objects.get(id = session_id)
        student.session_id = session_year
        
        student.save()
        
        messages.success(request,'Student Update is Successfuly')
        return redirect('view_student')
        
                  
        
    return render(request,'hod/edit_student.html')

def delete_student(request,admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,'Delete Successfuly')
    return redirect('view_student')

# Function for course

def add_course(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']
        
        course = Course(
            name = course_name,
        )
        
        course.save()
        messages.success(request, 'Course is Added Successfuly')
        return redirect('view_course')
    return render(request, 'hod/add_course.html')

def view_course(requset):
    course = Course.objects.all()
    context = {
        'course':course
    }
    return render(requset,'hod/view_course.html',context)

def edit_course(request,id):
    if request.method == 'POST':
        course = Course.objects.get(id = id)
        course.name = request.POST['course_name']
        course.save()
        messages.success(request,'Update is Success !')
        return redirect('view_course')
    else:
       course = Course.objects.get(id = id)
   
    return render(request,'hod/edit_course.html',{'info':course})

def delete_course(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request,'Course is Deleted Success !')
    return redirect('view_course')

# Function for Staff
def add_staff(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
                 
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"This email Already used")
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"This username Already used")
            return redirect('add_staff')
        
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=2                
            )
            user.set_password(password)
            user.save()
            
            staff = Staff(
                admin = user,
                gender=gender,
                address=address,
               
            )
            staff.save()
            messages.success(request,user.first_name + " " + user.last_name + " " + "are Successfuly Added")
            return redirect('view_staff')

    return render(request,'hod/add_staff.html')

def view_staff(request):
    staff = Staff.objects.all()
    context = {
        'staff':staff,
    }
        
    return render(request,'hod/view_staff.html',context)
def edit_staff(request,id):
    staff = Staff.objects.filter(id = id)
    
    context = {
        'staff':staff,
    }
    return render(request, 'hod/edit_staff.html',context)

def update_staff(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        user = CustomUser.objects.get(id = staff_id)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username
          
        if password !=None and password !="":
            user.set_password(password)
        if profile_pic !=None and profile_pic !="":
            user.profile_pic = profile_pic
            
        user.save()
        
        staff = Staff.objects.get(admin = staff_id)
        staff.gender=gender
        staff.address=address
        
        staff.save()
        
        messages.success(request,'Student Update is Successfull')
        return redirect('view_staff')
    return render(request, 'hod/edit_staff.html')

def delete_staff(request,admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request,'Delete Successfuly')
    return redirect('view_staff')

# Function for Subject
def add_subject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        
        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)
        
        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff,
        )
        
        subject.save()
        messages.success(request,'Subject are Successfuly Saved') 
        return redirect('view_subject')   
    
    context = {
        'course':course,
        'staff':staff
    }
    return render(request, 'hod/add_subject.html',context)

def view_subject(request):
    subject = Subject.objects.all()
    context = {
        'subject':subject
    }
    return render(request,'hod/view_subject.html',context)

def edit_subject(request,id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    context = {
        'subject':subject,
        'course':course,
        'staff':staff,
    }
    return render(request,'hod/edit_subject.html',context)
def update_subject(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)
        subject = Subject(
            id=subject_id,
            name=subject_name,
            course=course,
            staff=staff
        )
        subject.save()
        messages.success(request,'Subject are Successfuly Updated')
        return redirect('view_subject')
        
    return render(request,'hod/edit_subject.html')
def delete_subject(request,id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request,'Delete Successfull')
    return redirect('view_subject')
#------ Fucntion for Session -----------------
def add_session(request):
    if request.method == 'POST':
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('Session_year_end')
       
        session = Session_year(
            session_start=session_year_start,
            session_end=session_year_end
        )
        session.save()
        messages.success(request,'Session Add is Success')
        return redirect('view_session')
        
    return render(request, 'hod/add_session.html')

def view_session(request):
    session = Session_year.objects.all()
    context ={
        'session':session
    }
    return render(request, 'hod/view_session.html',context)

def edit_session(request,id):
    session = Session_year.objects.filter(id = id)
    context = {
        'session':session
    }
    return render(request,'hod/edit_session.html',context)
def update_session(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('Session_year_end')
        session = Session_year(
            id=session_id,
            session_start=session_year_start,
            session_end=session_year_end,
        )
        session.save()
        messages.success(request,'Update Success')
        return redirect('view_session')
        
    return render(request,'hod/edit_session.html')
def delete_session(request,id):
    session = Session_year.objects.get(id=id)
    session.delete()
    messages.success(request,'Delete Successfull')
    return redirect('view_session')
# Fucntion for Notification
def staff_send_notification(request):
    staff = Staff.objects.all()
    status = Staff_notification.objects.all().order_by('-id')[0:5]
    context = {
        'staff':staff,
        'status':status
    }
    return render(request,'hod/staff_notification.html',context)
def save_staff_notification(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')
        staff = Staff.objects.get(admin = staff_id)
        save_notification = Staff_notification(
            staff_id=staff,
            message=message,
        )
        save_notification.save()
        messages.success(request,'Message send Success')
        return redirect('staff_notification')
def Leave_veiew(request):
    staff_leave = Staff_leave.objects.all()
    context = {
        'staff_leave':staff_leave
    }
    return render(request,'hod/staff_leave.html',context)
def approve_leave(request,id):
    leave_approve = Staff_leave.objects.get(id = id)
    leave_approve.status = 1
    leave_approve.save()
    return redirect('staff_leave_veiew')
def reject_leave(request,id):
    leave_reject = Staff_leave.objects.get(id = id)
    leave_reject.status = 2
    leave_reject.save()
    return redirect('staff_leave_veiew')

def loan_veiew(request):
    loan_file = LoanDmand.objects.all()
    context = {
        'loan_file':loan_file
    }
    return render(request,'hod/loan_view.html',context)
def approve_loan(request,id):
    loan_approve = LoanDmand.objects.get(id = id)
    loan_approve.status = 1
    loan_approve.save()
    return redirect('loan_veiew')
def reject_loan(request,id):
    loan_reject = LoanDmand.objects.get(id = id)
    loan_reject.status = 2
    loan_reject.save()
    return redirect('loan_veiew')
    
    

    
    
    