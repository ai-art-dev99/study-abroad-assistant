from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class EducationDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gpa = models.PositiveIntegerField(default=0, blank=True)
    lastlevel = models.CharField(max_length=100, blank=True)
    field = models.CharField(max_length=250, blank=True)
    gradyear = models.DateField(null=True, blank=True)
    enlastedu = models.BooleanField(default=False, blank=True)
    workexp = models.PositiveIntegerField(default=0, blank=True)
    cv = models.FileField(default=None, upload_to='cv/', blank=True)
    sop = models.FileField(default=None, upload_to='sop/', blank=True)

class StudyPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    deslevel = models.CharField(max_length=250, blank=True)
    desprogram = models.CharField(max_length=250, blank=True)
    descity = models.CharField(max_length=250, blank=True)
    descountry = models.CharField(max_length=250, blank=True)

class LanguageProficiency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    testname = models.CharField(max_length=100, blank=True)
    testresult = models.CharField(max_length=300, blank=True)
    extratest = models.CharField(max_length=100, blank=True)
    extratestresult = models.CharField(max_length=300, blank=True)
    studynative = models.BooleanField(default=False, blank=True)
    studynativeyears = models.PositiveIntegerField(default=0, blank=True)

class WorkExperience(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expyears = models.PositiveBigIntegerField(default=0, blank=True)
    jobcv = models.FileField(default=None, upload_to='jobs/', blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ipaddr = models.GenericIPAddressField(default=None, null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    residence = models.CharField(max_length=100, blank=True)
    lang = models.CharField(max_length=50, blank=True)
    addressline = models.CharField(max_length=300, blank=True)
    postcode = models.CharField(max_length=50, blank=True)
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_education = EducationDetails(user=instance)
        user_lang = LanguageProficiency(user=instance)
        user_studypref = StudyPreferences(user=instance)
        user_work = WorkExperience(user=instance)
        user_profile = Profile(user=instance)
        user_education.save()
        user_lang.save()
        user_studypref.save()
        user_work.save()
        user_profile.save()

post_save.connect(create_profile, User)

class Program(models.Model):
    title = models.CharField(max_length=500, blank=True)
    progurl = models.URLField(blank=True)
    degree = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    duration = models.PositiveIntegerField(default=0, blank=True)
    startdate = models.DateField(null=True, blank=True)
    tuitionfee = models.PositiveBigIntegerField(default=0, blank=True)
    careerpathways = models.TextField(blank=True)
    adrequirements = models.TextField(blank=True)

class JobDetails(models.Model):
    title = models.CharField(max_length=250, blank=True)
    joburl = models.URLField(blank=True)
    company = models.CharField(max_length=350, blank=True)
    city = models.CharField(max_length=200, blank=True)
    jobtype = models.CharField(max_length=50, blank=True)
    contracttype = models.CharField(max_length=50, blank=True)
    salaryrange = models.CharField(max_length=50, blank=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    tasks = models.TextField(blank=True)

class Housing(models.Model):
    title = models.CharField(max_length=250, blank=True)
    housingtype = models.CharField(max_length=100, blank=True)
    location = models.TextField(blank=True)
    monthlyrent = models.PositiveBigIntegerField(default=0, blank=True)
    conditions = models.TextField(blank=True)
