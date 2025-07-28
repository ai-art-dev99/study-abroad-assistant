from django.contrib import admin
from users.models import Profile, EducationDetails, LanguageProficiency,\
                            StudyPreferences, Program, JobDetails, Housing
from django.contrib.auth.models import User

admin.site.register(Profile)
admin.site.register(EducationDetails)
admin.site.register(LanguageProficiency)
admin.site.register(StudyPreferences)
admin.site.register(Program)
admin.site.register(JobDetails)
admin.site.register(Housing)

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'country')

class JobDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'jobtype')

class HousingAdmin(admin.ModelAdmin):
    list_display = ('title', 'housingtype')

class ProfileInline(admin.StackedInline):
    model = Profile

class EducationInline(admin.StackedInline):
    model = EducationDetails

class LanguageInline(admin.StackedInline):
    model = LanguageProficiency

class StudyInline(admin.StackedInline):
    model = StudyPreferences

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'email']
    inlines = [ProfileInline, EducationInline, StudyInline, LanguageInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
