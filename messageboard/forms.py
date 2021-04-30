from django import forms
from django.forms.widgets import TextInput

# form for a user to start a new thread on the 
# messageboard
class createThreadForm (forms.Form):
    threadTopic = forms.CharField(label='Topic', widget=forms.TextInput(attrs={'class' : 'form-control', 'contenteditable' : 'true', 'placeholder' : 'Topic...'}))
    post_text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'contenteditable' : 'true', 'placeholder' : 'Topic...'}), label='First Post')

class createPostForm (forms.Form):
    mainText = forms.CharField(widget=forms.Textarea, label='Make Post')
    
