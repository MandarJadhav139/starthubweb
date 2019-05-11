# pylint: disable=E1101


from django.shortcuts import render, redirect
from .models import Startup
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ApplicationForm
from .models import Startup, Application
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import (TemplateView, ListView,
                                  DetailView, DeleteView,
                                  CreateView, UpdateView
                                  )

# Create your views here.


class StartupDetailView(DetailView):
    model = Startup
    template_name = 'detail.html'


class StartupListView(ListView):
    model = Startup
    template_name = 'list.html'


# class SignupView(CreateView):
#     form_class = SignupForm
#     template_name = 'signup.html'

#     success_url = reverse_lazy('app1:home')
#     # in order to login when signed up form_valid function of class createview is overwritten
#     # user is first saved without updating database
#     # because password is to be uploaded in hashed form
#     # by setpassword function password is hashed
#     # then user is saved to database

#     def form_valid(self, form):
#         valid = super().form_valid(form)
#         password = form.cleaned_data.get('password')
#         user = form.save(commit=False)
#         user.set_password(password)
#         user.save()
#         #user = authenticate(username=username, password=password)
#         login(self.request, user)
#         return valid

def SignupView(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        Email = request.POST.get('email')
        user = User.objects.create_user(
            username=Username, email=Email, password=Password)

        login(request, user)
        messages.success(request, 'Signup Successful')
        return HttpResponseRedirect(reverse('app1:home'))
    else:
        return render(request, 'signup.html')


def IndexView(request):
    return render(request, 'index.html')


def Login_View(request):
    # form = LoginForm()
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')

        user = authenticate(username=Username, password=Password)
        if user:
            login(request, user)
            messages.success(request, 'Login Successful')
            return HttpResponseRedirect(reverse('app1:home'))
        else:
            messages.error(request, "invalid info ")
            return HttpResponseRedirect(reverse('app1:home'))
    else:
        return render(request, 'login.html')


def SearchView(request):

    if request.method == 'POST':
        word = request.POST.get('searchbox')
        print(word)
    object_list = Startup.objects.filter(domain__iexact=word)
    return render(request, 'list.html', {'object_list': object_list})


@login_required
def Logout_View(request):
    logout(request)
    messages.success(request, 'Logged Out')
    return HttpResponseRedirect(reverse('index'))


@login_required
def ApplicationFormView(request):
    #form = ApplicationForm()

    if request.method == 'POST':
        # it is necessary to pass request.FILES as arguement or it will cause validation error
        # form = ApplicationForm(request.POST, request.FILES)
        name = request.POST.get('name')
        email = request.POST.get('email')
        github = request.POST.get('github')
        resume = request.POST.get('resume')

        application = Application.objects.create_application(
            name, email, github, resume)

        if application:

            messages.success(request, 'form filled successfully')
            return HttpResponseRedirect(reverse('app1:home'))
        else:
            messages.error(request, "invalid info ")
            return HttpResponseRedirect(reverse('app1:home'))

    else:
        return render(request, 'application_form.html')
