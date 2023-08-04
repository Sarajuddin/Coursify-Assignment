from django.shortcuts import render, redirect
from mainApp.models import Applicant
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='POST':
        obj = Applicant()
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.mobile = request.POST.get('mobile')
        obj.role = request.POST.get('role')
        obj.current_ctc = request.POST.get('current_ctc')
        obj.expected_ctc = request.POST.get('expected_ctc')
        obj.notice_period = request.POST.get('notice_period')
        obj.address1 = request.POST.get('address1')
        obj.address2 = request.POST.get('address2')
        obj.city = request.POST.get('city')
        obj.state = request.POST.get('state')
        obj.country = request.POST.get('country')
        obj.pincode = request.POST.get('pincode')
        obj.resume = request.POST.get('resume')
        obj.save()
        print('\nData Saved Successfully.....\n')
        messages.success(request, f"Thank You! Your response has been submitted")
        return redirect('/')
        # print('Data Saved Successfully.....')

    return render(request, 'index.html')