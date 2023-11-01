from typing import Any
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from formapp.forms import ReviewForm
from formapp.models import ReviewApp
from django.views import View
# this is for static templates but we can also pass dynamic content via context
from django.views.generic.base import TemplateView 
from django.views.generic.edit import FormView, CreateView # it will only create form and does not save in db automatically
from django.views.generic import ListView, DetailView
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
# class reviewes(View):
#     def get(self,request):
#         form = ReviewForm()
#         return render(request,'formapp/home.html',{'form':form})
#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/formapp/thank-you')

# this will save data using save method but we can also improve this
# class reviewes(FormView):
#     template_name = 'formapp/home.html'
#     form_class = ReviewForm
#     success_url = '/formapp/thank-you'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
        

class reviewes(CreateView):
    template_name = 'formapp/home.html'
    model = ReviewApp
    fields = '__all__'
    success_url = '/formapp/thank-you'


# class ThankyouView(View):
#     def get(self,request):
#         return render(request,'formapp/thank-you.html')


class ThankyouView(TemplateView):
    template_name = 'formapp/thank-you.html'
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Return dynamic data using template view get_context_data',
        return context
    

# class ReviewsListView(TemplateView):
#     template_name = 'formapp/reviews_list.html'
#     def get_context_data(self, **kwargs: Any):
#         context = super().get_context_data(**kwargs)
#         context['Reviews_List'] = ReviewApp.objects.all()
#         return context

class ReviewsListView(ListView):
    model = ReviewApp
    template_name = 'formapp/reviews_list.html'
    context_object_name = 'Reviews_List'
    

# class SingleReviwView(TemplateView):
#     template_name = 'formapp/review_detail.html'
#     def get_context_data(self, **kwargs: Any):
#         context = super().get_context_data(**kwargs)
#         review_id =  kwargs['id']
#         single_review = ReviewApp.objects.get(pk=review_id)
#         context['single'] = single_review
#         return context
    

class SingleReviewView(DetailView):
    model = ReviewApp
    template_name = 'formapp/review_detail.html'
    context_object_name = 'single'
