
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views,hod_views,staff_views,student_views,loan_views


urlpatterns = [
    # all url HOD panles
    path('admin/', admin.site.urls),
    # path('pdf/' , include('pdf.urls')),
    path('base/', views.base, name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='Logout'),
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),
    path('HOD/home', hod_views.HOME, name='hod_home'),
    path('HOD/student/add', hod_views.add_student, name='add_student'),
    path('HOD/student/view', hod_views.view_student, name='view_student'),
    path('HOD/student/edit/<str:id>', hod_views.edit_student, name='edit_student'),
    path('HOD/student/update', hod_views.update_student, name='update_student'),
    path('HOD/student/delete/<str:admin>', hod_views.delete_student, name='delete_student'),
    # Url for Staff
    path('HOD/staff/add', hod_views.add_staff, name='add_staff'),
    path('HOD/staff/view', hod_views.view_staff, name='view_staff'),
    path('HOD/staff/edit/<str:id>', hod_views.edit_staff, name='edit_staff'),
    path('HOD/staff/update', hod_views.update_staff, name='update_staff'),
    path('HOD/staff/delete/<str:admin>', hod_views.delete_staff, name='delete_staff'),
    # Url for Course
    path('HOD/course/add', hod_views.add_course, name='add_course'),
    path('HOD/course/view', hod_views.view_course, name='view_course'),
    path('HOD/course/edit/<str:id>', hod_views.edit_course, name='edit_course'),
    path('HOD/course/delete/<str:id>', hod_views.delete_course, name='delete_course'),
    # Url for Subject
    path('HOD/subject/add', hod_views.add_subject, name='add_subject'),
    path('HOD/subject/view', hod_views.view_subject, name='view_subject'),
    path('HOD/subject/edit/<str:id>', hod_views.edit_subject, name='edit_subject'),
    path('HOD/subject/update', hod_views.update_subject, name='update_subject'),
    path('HOD/subject/delete/<str:id>', hod_views.delete_subject, name='delete_subject'),
    #----------Url for Session ------------------
    path('HOD/session/add', hod_views.add_session, name='add_session'), 
    path('HOD/session/view', hod_views.view_session, name='view_session'),
    path('HOD/session/edit/<str:id>', hod_views.edit_session, name='edit_session'),
    path('HOD/session/update', hod_views.update_session, name='update_session'),
    path('HOD/session/delete/<str:id>', hod_views.delete_session, name='delete_session'),
    path('HOD/staff/send_notification', hod_views.staff_send_notification, name='staff_notification'),
    path('HOD/staff/save_staff_notification', hod_views.save_staff_notification, name='save_staff_notification'),
    path('HOD/staff/leave_veiew', hod_views.Leave_veiew, name='staff_leave_veiew'),
    path('HOD/staff/approve_leave/<str:id>', hod_views.approve_leave, name='staff_leave_approve'),
    path('HOD/staff/reject_leave/<str:id>', hod_views.reject_leave, name='staff_leave_reject'),
    
    # all url for Staff Panles
    path('STAFF/home', staff_views.HOME, name='staff_home'),
    path('STAFF/notification', staff_views.NOTIFICATION, name='notification'),
    path('STAFF/staff_mark_done/<str:status>', staff_views.staff_done, name='staff_done'),
    path('STAFF/apply_leave_staff', staff_views.STAFF_LEAVE_APPLY, name='leave_staff'),
    path('STAFF/apply_leave_save', staff_views.staff_leave_save, name='staff_leave_save'),
    
    # all Url for Loan Demand Class
    path('STAFF/loan_status', staff_views.loan_status, name='loan_status'),
    path('STAFF/loan_demand', staff_views.loan_demand, name='loan_demand'),
    path('HOD/STAFF/loan_veiew', hod_views.loan_veiew, name='loan_veiew'),
    path('HOD/staff/approve_loan/<str:id>', hod_views.approve_loan, name='loan_approve'),
    path('HOD/staff/reject_loan/<str:id>', hod_views.reject_loan, name='loan_reject'),
    path('STAFF/loan_tamasuk/<str:id>', staff_views.loan_tamasuk, name='loan_tamasuk'),
    path('STAFF/creare_pdf', staff_views.pdf_report, name='creare_pdf'),
 
    
   
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
