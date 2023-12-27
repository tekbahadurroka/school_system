# from django.shortcuts import render
# from loan_demand.models import LoanDmand
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

# # Create your views here.
# def loan_status(request):
#     loan_status = LoanDmand.objects.all()
#     context = {
#         'loan_status':loan_status
#     }
#     return render(request,'pdf_convert/loan_action.html',context)
# def showinfo(request,id):
#    showinfo = LoanDmand.objects.filter(id=id)
#    context = {
#       'showinfo':showinfo
#    }  
#    return render(request,'pdf_convert/showinfo.html',context)
 
# def pdf_report(request):
#     pdf_report_view = LoanDmand.objects.all()
#     template_path = 'pdf_convert/report.html'
#     context = {'pdf_report_view': pdf_report_view}
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="tamasuk.pdf"'
#     template = get_template(template_path)
#     html = template.render(context)

#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     # if error then show some funny view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response
   