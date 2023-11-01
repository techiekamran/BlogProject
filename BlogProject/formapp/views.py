from django.shortcuts import render
from django.http import HttpResponseRedirect
from formapp.forms import ReviewForm
from formapp.models import ReviewApp
from django.views import View
# Create your views here.



# def reviews(request):
#     return render(request,'formapp/home.html')

# def thank_you(request):
#     return render(request,'formapp/thank-you.html')

# def reviews(request):
#     if request.method == "POST":
#         created_user = request.POST['username']
#         if created_user =="":
#             return render(request,'formapp/home.html',{'has_error':True})
#         print(created_user)
#         return HttpResponseRedirect('/formapp/thank-you')
#     return render(request,'formapp/home.html',{'has_error':False})

# def thank_you(request):
#     return render(request,'formapp/thank-you.html')

#django form

# def reviews(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)

#         #we can also save form model directly because we have already added into forms class meta
#         if form.is_valid():
#             form.save()
#             # data = ReviewApp(username=form.cleaned_data['username'],
#             #                  review_text=form.cleaned_data['review_text'],
#             #                  rating=form.cleaned_data['rating'],)
#             # data.save()
#             #print(form.cleaned_data)
#             return HttpResponseRedirect('/formapp/thank-you')
#     else:
#         form = ReviewForm()
#     return render(request,'formapp/home.html',{'form':form})

# def thank_you(request):
#     return render(request,'formapp/thank-you.html')

#using class based view
#ReviewView convention
class reviewes(View):
    def get(self,request):
        form = ReviewForm()
        return render(request,'formapp/home.html',{'form':form})
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/formapp/thank-you')
        


class ThankyouView(View):
    def get(self,request):
        return render(request,'formapp/thank-you.html')