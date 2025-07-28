from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from users.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", 
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control m-2',
                                 'placeholder': 'Please enter your email'
                                 }))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'email'
    }), required=False)
    nationality = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'nationality'
    }), required=False)
    residence = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'residence'
    }), required=False)
    lang = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'language'
    }), required=False)
    addressline = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'address line'
    }), required=False)
    postcode = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'post code'
    }), required=False)

    class Meta:
        model = Profile
        fields = ('email', 'nationality', 'residence', 
                  'lang', 'addressline', 'postcode',)
        

class UserPreferencesForm(forms.ModelForm):
    deslevel = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'degree'
    }), required=False)
    desprogram = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'language'
    }), required=False)
    descity = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'nationality'
    }), required=False)
    descountry = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'residence'
    }), required=False)

    class Meta:
        model = Profile
        fields = ('deslevel', 'desprogram', 'descity', 'descountry',)
        

class UserEducationForm(forms.ModelForm):
    gpa = forms.IntegerField(label='GPA', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'gpa (4, 100, 20, etc.)'
    }), required=False)
    lastlevel = forms.CharField(label='last level', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'last level education'
    }), required=False)
    field = forms.CharField(label='field', widget=forms.TextInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'field'
    }), required=False)
    gradyear = forms.DateField(label='graduation year', widget=forms.DateInput(
        format="%Y-%m-%d", 
        attrs={'class': 'form-control m-2', "type": "date"}
    ), required=False)
    enlastedu = forms.BooleanField(label='was your last level of education in english?',
                                   required=False)
    workexp = forms.IntegerField(label='', widget=forms.NumberInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'how many years of work experience'
    }), required=False)
    cv = forms.FileField(label='', widget=forms.FileInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'you can upload your cv'
    }), required=False)
    sop = forms.FileField(label='', widget=forms.FileInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'you can upload your sop'
    }), required=False)

    class Meta:
        model = Profile
        fields = ('gpa', 'lastlevel', 'field', 
                  'gradyear', 'enlastedu', 'workexp',
                  'cv', 'sop',)
        

class UserWorkForm(forms.ModelForm):
    expyears = forms.IntegerField(label='how many years of experience you got', 
                                  widget=forms.NumberInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'email'
    }), required=False)
    jobcv = forms.FileField(label='upload your work cv', widget=forms.FileInput(attrs={
        'class': 'form-control m-2',
        'placeholder': 'degree'
    }), required=False)

    class Meta:
        model = Profile
        fields = ('expyears', 'jobcv',)
