from django import forms
from profilepage.models import Course, Profile

class add_course_form(forms.Form):
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['add_course'].choices = [(x, x) for x in Course.objects.difference(current_user.profile.courses.all())]
    #populate choices with all courses not taken by the user
    add_course = forms.ChoiceField(label="Add a course")
    #, choices=[(x, x) for x in Course.objects.difference(current_user.profile.courses.all())]

class remove_course_form(forms.Form):
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['remove_course'].choices = [(x, x) for x in current_user.profile.courses.all()]
    #populate choices with all of the user's courses
    remove_course = forms.ChoiceField(label="Remove a Course")
    #, choices=[(x, x) for x in current_user.profile.courses.all()]