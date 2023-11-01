from django.urls import path
from formapp import views
from formapp.views import reviewes, ThankyouView
urlpatterns = [
    path('',reviewes.as_view(),name='reviews'),
    path('thank-you',ThankyouView.as_view(),name='thanks'),
    #path('',views.reviews,name='reviews'), for function based views
    #path('thank-you',views.thank_you,name="thanks"), function based views
]

