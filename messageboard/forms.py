from django import forms
from django.forms.widgets import TextInput

# form for a user to start a new thread on the 
# messageboard
class createThreadForm (forms.Form):
    threadTopic = forms.CharField(label='Topic')
    post_text = forms.CharField(widget=forms.Textarea, label='First Post')

class createPostForm (forms.Form):
    mainText = forms.CharField(widget=forms.Textarea, label='Make Post')
    
