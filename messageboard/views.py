from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse

from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Import "from post.models" all the models from the threads and posts
# in Ryan's message & post database branch
from posts.models import Thread
from posts.models import Post
from .forms import createThreadForm
from .forms import createPostForm


# Basic http response used for debugging
def basicResponse (request):
    return HttpResponse("Success")


# View of the main messageboard with NO thread selected
def mainBoard (request):
    # Get all threads
    context = {}
    context['userid'] = request.user
    context['threadList'] = list(Thread.objects.all())
    context['currentThreadNum'] = None
    context['currentThread'] = None
    context['posts'] = []
    context['orig_posts'] = list(Post.objects.filter(post_ID=0))
    return render(request, "board.html", context)


# View of the main messageboard WITH a thread selected
def getThreadPosts (request, thrdID):

    # Check if user is making a post to the current thread
    if request.method == 'POST':
        # Make a local form object and populate it with the raw info sent to us in the request
        form = createPostForm(request.POST)
        
        # Check if form entries are valid
        if form.is_valid():
            # Get latest created post and its unique post ID within the thread
            try:
                latestPost = Post.objects.filter(thread__thread_ID__exact=thrdID).latest('post_date')
                postID = latestPost.post_ID + 1
            except:
                postID = 0

            # Get the validated post text
            post_main_text = form.cleaned_data['mainText']

            # Create new post obeject to be inserted into database
            this_thread = Thread.objects.get(thread_ID=thrdID)
            post_entry = Post.objects.create(main_text = post_main_text, thread = this_thread, post_ID = postID, owning_thread_ID = thrdID, username=request.user.username)
            
            # Save the newly created post in the database
            post_entry.save()



    # Get all posts in the selected thread and list of all threads
    context = {}
    context['threadList'] = list(Thread.objects.all())
    context['numberThreads'] = len(context['threadList'])
    # Check if messageboard has thread with ID requested: If not, then redirect 
    # to default messageboard.
    try:
        th = Thread.objects.get(thread_ID=thrdID)
    except:
        redirectPage = "/messageboard/"
        context['posts'] = []
        context['orig_posts'] = list(Post.objects.filter(post_ID=0))
        context['currentThreadNum'] = 1
        context['currentThread'] = None
        context['userid'] = request.user
        return render(request, 'board.html', context)

    # Attempt to get posts pertaining to thread. If no posts (supposed to be impossible
    # because each thread has a starting post), then return a blank list.
    try:
        postList = list(Post.objects.all())
    except:
        context['posts'] = []
        context['userid'] = request.user
        return render(request, 'board.html', context)
    
    # Render the messageboard with all the posts from the currently selected thread
    context['userid'] = request.user
    context['currentThreadNum'] = thrdID
    context['currentThread'] = Thread.objects.get(thread_ID=thrdID)
    postList = list(Post.objects.filter(thread__thread_ID__exact=thrdID))
    context['posts'] = postList
    context['form'] = createPostForm()
    context['orig_posts'] = list(Post.objects.filter(post_ID=0))
    return render(request, 'board.html', context)


# View which allows a users to create a new thread
def userMakesThread (request):

    # Check if request in a POST request, else get a blank form.
    #
    # Basically: "Is the client sending us a form they filled in(POST)? If not then 
    # send them a blank form to fill out(GET)."
    if request.method == 'POST':

        # Make a local form object and populate it with the raw info sent to us in the request
        form = createThreadForm(request.POST)

        # Check if form entries are valid
        if form.is_valid():
            # Get latest created thread and its unique thread ID
            try:
                latestThread = Thread.objects.latest('thread_date')
                thrdID = latestThread.thread_ID + 1
            except:
                thrdID = 1

            # Get the validated post text and thread topic
            thrdTopic = form.cleaned_data['threadTopic']
            post_main_text = form.cleaned_data['post_text']

            # Create new thread and post obejects to be inserted into database
            thread_entry = Thread.objects.create(thread_ID = thrdID, threadTopic = thrdTopic, currentPostNumber = 1, main_post_id = 0)
            post_entry = Post.objects.create(main_text = post_main_text, thread = thread_entry, post_ID = 0, owning_thread_ID = thrdID, username=request.user.username)
            
            # Save the newly created thread and post in the database
            thread_entry.save()
            post_entry.save()
            theURL = "/messageboard/thread/" + str(thrdID) + "/"
            return redirect(theURL)

    # Get request used and blank form is given to client
    else:
        form = createThreadForm()

    # Create a context for returning to the messageboard with the new thread
    context = {}
    context['form'] = form
    return render(request, 'newThread.html', context)


# ****************** DEPRECATED ******************
# View which allows a users to create a new post
# ************************************************
def userMakesPost (request, thrdID):

    # Check if request in a POST request, else get a blank form.
    if request.method == 'POST':

        # Make a local form object and populate it with the raw info sent to us in the request
        form = createPostForm(request.POST)

        # Check if form entries are valid
        if form.is_valid():
            # Get latest created post and its unique post ID within the thread
            try:
                latestPost = Post.objects.filter(thread__thread_ID__exact=thrdID).latest('post_date')
                postID = latestPost.post_ID + 1
            except:
                postID = 0

            # Get the validated post text
            post_main_text = form.cleaned_data['mainText']

            # Create new post obeject to be inserted into database
            this_thread = Thread.objects.get(thread_ID=thrdID)
            post_entry = Post.objects.create(main_text = post_main_text, thread = this_thread, post_ID = postID, owning_thread_ID = thrdID)
            
            # Save the newly created post in the database
            post_entry.save()
            
            # Create a context for returning to the messageboard with the new thread
            context = {}
            context['currentThread'] = thrdID
            context['posts'] = list(Post.objects.filter(thread__thread_ID__exact=thrdID))
            context['threadList'] = Thread.objects.all()
            theURL = "/messageboard/thread/" + str(thrdID) + "/"
            return redirect(theURL)#render(request, 'board.html', context)

    # Get request used and blank form is given to client
    else:
        form = createPostForm()

    # Create a context for returning to the messageboard with the new thread
    context = {}
    context['form'] = form
    return render(request, 'newPost.html', context)