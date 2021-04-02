# from django.shortcuts import render
# from django.http import JsonResponse
#
# from django.http import HttpResponse
# from django.http import HttpResponseRedirect
#
# # Import "from post.models" all the models from the threads and posts
# # in Ryan's message & post database branch
# from .forms import createThreadForm
#
#
# # Basic http response used for debugging
# def basicResponse (request):
#     return HttpResponse("Success")
#
#
# # View of the main messageboard with NO thread selected
# def mainBoard (request):
#     # Get all threads
#     context = {}
#     context['threadList'] = tempThreadModel.objects.all()
#     context['posts'] = {}
#     return render(request, "board.html", context)
#
#
# # View of the main messageboard WITH a thread selected
# def getThreadPosts (request, thrdID):
#
#     # Get all posts in the selected thread and list of all threads
#     context = {}
#     context['threadList'] = tempThreadModel.objects.all() #
#     context['posts'] = models.tempPosts.objects.all(threadID=thrdID) # post.thread.all(thread)
#     return (request, 'board.html', context)
#
#
# # View which allows a users to create a new thread
# def userMakesThread (request):
#
#     # Check if request in a POST request, else do nothing
#     if request.method == 'POST':
#         form = createThreadForm(request.POST)
#
#         # Check if form entries are valid
#         if form.is_valid():
#             # Get latest created thread and its unique thread ID
#             latestThread = Thread.objects.latest('thread_date')
#             thrdID = latestThread.thread_ID + 1
#
#             # Get the validated post text and thread topic
#             thrdTopic = form.cleaned_data['threadTopic']
#             post_main_text = form.cleaned_data['post_text']
#
#             # Create new thread and post obejects to be inserted into database
#             thread_entry = Thread.objects.create(thread_ID = thrdID, threadTopic = mainText, currentPostNumber = 1, main_post_id = 0)
#             post_entry = Post.objects.create(main_text = post_main_text, thread = thread_entry, post_ID = 0)
#
#             # Save the newly created thread and post in the database
#             thread_entry.save()
#             post_entry()
#
#             # Create a context for returning to the messageboard with the new thread
#             context = {}
#             context['posts'] = post_entry
#             context['threadList'] = tempThreadModel.objects.all()
#
#             return (request, 'board.html', context)
#     # Get request used
#     else:
#         pass