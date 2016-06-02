from django.shortcuts import render
from User.models import UserProfile
from User.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'page/index.html', {})
def about(request):
    return render(request, 'page/about.html', {})
def codes(request):
    return render(request, 'page/codes.html', {})
def contact(request):
    return render(request, 'page/contact.html', {})
def gallery(request):
    return render(request, 'page/gallery.html', {})
def baidumap(request):
    return render(request, 'page/baidumap.html', {})

def login(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'page/login.html', context_dict)






def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'page/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

def base(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'page/base.html', context_dict)

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user')
            else:
                return HttpResponse("Your register account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            # return HttpResponse("Invalid login details supplied.")
            context['status'] = "Invalid login details supplied."
            # status = "Invalid login details supplied."
            # return HttpResponseRedirect('/register/')
            return render(request, 'page/login.html', context)
    else:
        return render(request, 'page/login.html', context)
# Create your views here.

def some_view(request):
    if request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/register')

