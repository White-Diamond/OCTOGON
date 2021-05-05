from django.shortcuts import render, get_object_or_404, redirect

from profilepage.models import Course, Profile
from .forms import add_course_form, remove_course_form

# Create your views here.
def course_selection(request):
    current_user = request.user
    # if current_user.is_authenticated
    context = {}
    return render(request, "course_selection.html", context)

def add_course(request):
    current_user = request.user
    if request.method == 'POST':
        context = {}
        form = add_course_form(request.POST, user=request.user)
        context['form'] = form
        if form.is_valid():
            course_name = form.cleaned_data['add_course']
            course = Course.objects.get(name_short=course_name)
            request.user.profile.courses.add(course)
            request.user.save()
            return render(request, "add_course.html", context)
    else:
        form = add_course_form(user=request.user)
    context = {}
    context['form'] = form
    return render(request, "add_course.html", context)
def remove_course(request):
    current_user = request.user
    if request.method == 'POST':
        context = {}
        form = remove_course_form(request.POST, user=request.user)
        context['form'] = form
        if form.is_valid():
            course_name = form.cleaned_data['remove_course']
            course = Course.objects.get(name_short=course_name)
            request.user.profile.courses.remove(course)
            request.user.save()
            return render(request, "remove_course.html", context)
    else:
        form = remove_course_form(user=request.user)
    context = {}
    context['form'] = form
    return render(request, "remove_course.html", context)