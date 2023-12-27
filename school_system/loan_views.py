from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from loan_demand.models import LoanDmand

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
        tpropose = request.POST.get('client_name')
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
        
    return render(request,'loan/loan_demand.html')

# def approve_leave(request,id):
#     leave_approve = Staff_leave.objects.get(id = id)
#     leave_approve.status = 1
#     leave_approve.save()
#     return redirect('staff_leave_veiew')
# def reject_leave(request,id):
#     leave_reject = Staff_leave.objects.get(id = id)
#     leave_reject.status = 2
#     leave_reject.save()
#     return redirect('staff_leave_veiew')