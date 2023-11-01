from django import forms
from formapp.models import ReviewApp

#using forms

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your Name: ",max_length=10,error_messages={
#         'required':'Your name can not be empty',
#         'max_length':'Length must be 10',})
#     review_text = forms.CharField(label='Your Feedback',widget=forms.Textarea,max_length=200)
#     rating = forms.IntegerField(label='Your Rating',min_value=1,max_value=5)


#using django model form

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewApp
        fields = '__all__'
        #exclude = ['username']
        labels = {
            'username': 'Please enter your username',
            'review_text': 'Give us Feedback',
            'rating': 'Share your rating',
        }
