from django import forms

class createThreadForm (form.Form):
    threadTopic = forms.CharField()
    messageContents = forms.TextInput()
    userID = forms.IntegerField()

