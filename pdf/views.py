from django.shortcuts import render
from .models import Profile

from django.http import HttpResponse
from django.template import loader
import pdfkit
import io
# Create your views here.

def index(request):
    if request.method=='POST':
        company_addr=request.POST.get("company_addr","")
        company_name=request.POST.get("company_name","")
        your_addr=request.POST.get("your_addr","")
        your_name=request.POST.get("your_name","")
        subject=request.POST.get("subject","")
        campus_name=request.POST.get("campus_name","")
        skill=request.POST.get("skill","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        d_year=request.POST.get("d_year","")
        d_month=request.POST.get("d_month","")
        d_day=request.POST.get("d_day","")
        image=request.POST.get("image","")
        
        
        
        profile=Profile(company_addr=company_addr,company_name=company_name,
                your_addr=your_addr,your_name=your_name,subject=subject,
                campus_name=campus_name,skill=skill,phone=phone,email=email,d_year=d_year,d_month=d_month,d_day=d_day,image=image)
        profile.save()
        
    return render(request,'form.html')


def coverletter(request, id):
    pro=Profile.objects.get(pk=id) 
    template=loader.get_template('coverletter.html')
    html=template.render({'pro':pro})
    option={
        'page-size':'Letter',
        'encoding': 'UTF-8'
    }
    pdf=pdfkit.from_string(html,False,option)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    
    return response

    return render(request,'coverletter.html',{'pro':pro})


def list(request):
    profiles=Profile.objects.all()
    
    return render(request,'list.html',{'profiles':profiles})
    
    
    
