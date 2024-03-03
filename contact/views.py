from django.shortcuts import render, redirect
# from .forms import UserRegisterForm
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserRegisterForm
from contact.forms import ContactForm
from .models import Profile
from django.contrib import messages
# your views here.
def index(request):
    return render (request, 'index.html')

# contact
def contact(request):

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render (request, 'contact.html', {'form': form})

#about
def about(request):
    return render (request, 'about.html')

#signin view
class UserSignInView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# def profile(request):
#     form = ProfileForm(instance=request.user.profile) 
#     # UserRegisterForm.object.get_or_create(UserRegisterForm=request.user)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     # else:
#     #     form = ProfileForm(instance=request.user.profile)

#     return render(request, 'profile.html', {'form': form})

#profile view
@login_required
def profile(request):
    user = request.user
    try:
        profile = user.profile
        form = ProfileForm(instance=request.user.profile) 
        # UserRegisterForm.object.get_or_create(UserRegisterForm=request.user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=request.user.profile)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = ProfileForm(instance=request.user.profile)
  
    except Profile.DoesNotExist:
        # Create the profile
        profile = Profile.objects.create(user=user)
        form = ProfileForm(instance=request.user.profile) 
        # UserRegisterForm.object.get_or_create(UserRegisterForm=request.user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=request.user.profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile was updated successfully!')
                return redirect('profile')
        else:
            form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'profile': profile, 'form': form})