# pylint: disable=E1101


from django.shortcuts import render
from .models import Startup
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, ApplicationForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

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


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'

    success_url = reverse_lazy('app1:home')
    # in order to login when signed up form_valid function of class createview is overwritten
    # user is first saved without updating database
    # because password is to be uploaded in hashed form
    # by setpassword function password is hashed
    # then user is saved to database

    def form_valid(self, form):
        valid = super().form_valid(form)
        password = form.cleaned_data.get('password')
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        #user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid


def IndexView(request):
    return render(request, 'index.html')


def Login_View(request):
    form = LoginForm()
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')

        user = authenticate(username=Username, password=Password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('app1:home'))
        else:
            return HttpResponse("username : {} password :{}  user:{} is not valid".format(Username, Password, user))
    else:
        return render(request, 'login.html', {'form': form})


@login_required
def Logout_View(request):
    logout(request)
    return HttpResponseRedirect(reverse('app1:home'))


@login_required
def ApplicationFormView(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(data=request.POST)

        if form.is_valid():
            if 'resume' in request.FILES:
                profile = form.save(commit=False)
                profile.resume = request.files['resume']
            form.save(commit=True)
            return HttpResponseRedirect(reverse('app1:home'))
        else:
            return HttpResponse("invalid form {}".format(form.errors))
    else:
        return render(request, 'application_form.html', {'form': form})
