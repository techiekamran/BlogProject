from django.urls import path
from formapp import views
from formapp.views import reviewes, ThankyouView,ReviewsListView, SingleReviewView
urlpatterns = [
    path('',reviewes.as_view(),name='reviews'),
    path('thank-you',ThankyouView.as_view(),name='thanks'),
    path('reviews_list',ReviewsListView.as_view(),name='review-list'),
    path('single_review/<int:pk>',SingleReviewView.as_view(),name='singlereview'),
    #path('single_review/<int:id>',SingleReviewView.as_view(),name='singlereview'),
    #path('',views.reviews,name='reviews'), for function based views
    #path('thank-you',views.thank_you,name="thanks"), function based views
]

