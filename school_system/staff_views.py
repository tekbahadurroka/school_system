from django.shortcuts import render,redirect
from django.contrib import messages
from loan_demand.models import LoanDmand
from schoolapp.models import Staff,Staff_notification,Staff_leave
from loan_demand.models import LoanDmand
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def HOME(request):
    
    return render(request, 'staff/home.html')

def NOTIFICATION(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id=i.id
        
        notification = Staff_notification.objects.filter(staff_id=staff_id)
        context = {
            'notification':notification
        }
    return render(request,'staff/notification.html',context)
def staff_done(request,status):
    notification = Staff_notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notification')

def STAFF_LEAVE_APPLY(request):
    s_leave = Staff.objects.filter(admin = request.user.id)
    
    for i in s_leave:
        staff_id = i.id
        leave_history = Staff_leave.objects.filter(staff_id = staff_id)
        
        context = {
            'leave_history':leave_history
        }
    return render(request,'staff/apply_leave.html',context)

def staff_leave_save(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        region = request.POST.get('region')
        staff = Staff.objects.get(admin = request.user.id)
        leave = Staff_leave(
            staff_id=staff,
            date=start_date,
            date_end=end_date,
            message=region,
           
          
        )
        leave.save()
        messages.success(request,'Leave apply Success')
        return redirect('leave_staff')
# Loan Demand

def loan_status(request):
    loan_status = LoanDmand.objects.all()
    context = {
        'loan_status':loan_status
    }
    return render(request,'staff/loan_status.html',context)
def loan_demand(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        client_name = request.POST.get('client_name')
        ctizenship_no = request.POST.get('ctizenship_no')
        issue_date = request.POST.get('issue_date')
        issue_place = request.POST.get('issue_place')
        client_age = request.POST.get('client_age')
        grend_name = request.POST.get('grend_name')
        husband_name = request.POST.get('husband_name')
        village = request.POST.get('village')
        worda = request.POST.get('worda')
        address = request.POST.get('address')
        district = request.POST.get('district')
        province = request.POST.get('province')
        country = request.POST.get('country')
        tvillage = request.POST.get('tvillage')
        tworda = request.POST.get('tworda')
        taddress = request.POST.get('taddress')
        tdistrict = request.POST.get('tdistrict')
        tprovince = request.POST.get('tprovince')
        tcountry = request.POST.get('tcountry')
        tpropose = request.POST.get('tpropose')
        loan_amount = request.POST.get('loan_amount')
        loan_word = request.POST.get('loan_word')
        maturity_date = request.POST.get('maturity_date')
        document = request.FILES.get('document')
        data = LoanDmand(
            loan_no = client_id,
            name = client_name,
            old_country = country,
            old_district = district,
            old_municipilaty = address,
            old_word_no = worda,
            old_village = village,
            zone = province,
            country = tcountry,
            province = tprovince,
            district = tdistrict,
            municipilaty = taddress,
            word_no = tworda,
            village = tvillage,
            greand_father = grend_name,
            father_husband = husband_name,
            citizenship_no = ctizenship_no,
            issue_place = issue_place,
            isssue_date = issue_date,
            age = client_age,
            loan_amount = loan_amount,
            loan_text = loan_word,
            maturity_age = maturity_date,
            propose = tpropose,
            document = document,
        )
        data.save()
        messages.success(request, 'Loan Request is success')
        return redirect('loan_demand')
    return render(request,'staff/loan_demand.html')
def loan_tamasuk(request,id):
    tamasuk = LoanDmand.objects.filter(id=id)
    context = {
        'tamasuk':tamasuk
    }  
    return render(request,'staff/loan_tamasuk.html',context)   
    
def pdf_report(request):
    pdf_report_view = LoanDmand.objects.all()
    template_path = 'staff/report.html'
    context = {'pdf_report_view': pdf_report_view}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="tamasuk.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response