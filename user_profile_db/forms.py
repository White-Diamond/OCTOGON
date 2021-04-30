from django import forms

class add_course_form(forms.Form):
    #populate choices with all courses not taken by the user
    add_course = forms.ChoiceField(label="Add a course", choices=[(x, x) for x in Course.objects.difference(current_user.profile.courses.all())])

class remove_course_form(forms.Form):
    #populate choices with all of the user's courses
    remove_course = forms.ChoiceField(label="Remove a Course", choices=[(x, x) for x in current_user.profile.courses.all()])