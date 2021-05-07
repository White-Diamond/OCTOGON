from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
  def wrapper_func(request, *args, **kwargs):
      if not request.user.is_authenticated:
        return redirect("home")
      return view_func(request, *args, **kwargs)
  return wrapper_func

def authenticated_user(view_func):
  def wrapper_func(request, *args, **kwargs):
      if request.user.is_authenticated:
        return redirect("home")
      return view_func(request, *args, **kwargs)
  return wrapper_func

# function call ex: @allowed_users(allowed_roles=['admin', 'student'])
# IMPORTANT: Must create groups in the admin page
def allowed_users(allowed_roles=[]):
  def decorator(view_func):
    def wrapper_func(request, *args, **kwargs):

      group = None
      if request.user.groups.exists():
        group = request.user.groups.all()[0].name

      if group in allowed_roles:
        return view_func(request, *args, **kwargs)

      return HttpResponse("You are not authorized to view this page")
    return wrapper_func
  return decorator
