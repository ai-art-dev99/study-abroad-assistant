from django.shortcuts import render, redirect
from users.forms import SignUpForm, UserProfileForm, \
                          UserPreferencesForm, UserWorkForm, UserEducationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from users.models import Profile, EducationDetails, \
                          StudyPreferences, WorkExperience
import json

def register(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('chat')
  else:
    form = SignUpForm()
  return render(request, 'register.html', {'form': form})

def login_user(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('chat')
  return render(request, 'login.html')

def logout_user(request):
  logout(request)
  return redirect('login')

def update_profile(request):
  if request.user.is_authenticated:
    current_user = Profile.objects.get(user__id=request.user.id)
    form = UserProfileForm(request.POST or None, instance=current_user)
    if form.is_valid():
      form.save()
      return redirect('account')
  return render(request, 'update_info.html', {'form':form})

def update_preferences(request):
  if request.user.is_authenticated:
    current_user = StudyPreferences.objects.get(user__id=request.user.id)
    form = UserPreferencesForm(request.POST or None, instance=current_user)
    if form.is_valid():
      form.save()
      return redirect('account')
  return render(request, 'update_info.html', {'form':form})

def update_education(request):
  if request.user.is_authenticated:
    current_user = EducationDetails.objects.get(user__id=request.user.id)
    form = UserEducationForm(request.POST or None,
                             request.FILES or None, 
                             instance=current_user)
    if form.is_valid():
      form.save()
      return redirect('account')
  return render(request, 'update_info.html', {'form':form})

def update_work(request):
  if request.user.is_authenticated:
    current_user = WorkExperience.objects.get(user__id=request.user.id)
    form = UserWorkForm(request.POST or None, 
                        request.FILES or None,
                        instance=current_user)
    if form.is_valid():
      form.save()
      return redirect('account')
  return render(request, 'update_info.html', {'form':form})
    
def account(request):
  context = {}
  if request.user.is_authenticated:
    user = User.objects.get(id=request.user.id)
    user_profile = Profile.objects.get(user__id=request.user.id)
    user_studypreference = StudyPreferences.objects.get(user__id=request.user.id)
    user_workexperience = WorkExperience.objects.get(user__id=request.user.id)
    user_educationdetails = EducationDetails.objects.get(user__id=request.user.id)
    context = {
      'user': user,
      'profile': user_profile,
      'study': user_studypreference,
      'work': user_workexperience,
      'education': user_educationdetails
    }
  return render(request, 'account.html', context=context)
