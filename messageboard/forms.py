from django import forms

# form for a user to start a new thread on the 
# messageboard
class createThreadForm (forms.Form):
    threadTopic = forms.CharField()
    post_text = forms.TextInput()
    