from django.shortcuts import render, get_object_or_404, redirect

from .models import Course, Profile
from .forms import add_course_form, remove_course_form

# Create your views here.
# def class_selection(request):
    # current_user = request.user
    # # if current_user.is_authenticated
    # context = {}
    # return render(request, "class_selection.html", context)
def add_class(request):
    if request.method == 'POST':
        form = add_course_form(request.POST)
        if form.is_valid():
        
def remove_class(request):
	if request.method == 'POST':
		form = remove_course_form(request.POST)
		if form.is_valid():
		