from django.urls import path
from .views import views, user_views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login_user, name='login'),
    path('logout/', user_views.logout_user, name='logout'),
    path('account/', user_views.account, name='account'),
    path('update-profile', user_views.update_profile, name='update-profile'),
    path('update-userpreferences', user_views.update_preferences, name='update-userpreferences'),
    path('update-usereducation', user_views.update_education, name='update-usereducation'),
    path('update-userwork', user_views.update_work, name='update-userwork'),
    path('gpt-feedback/', views.pdf_feedback, name='gpt-feedback'),
    path('programs/', views.programs, name='programs'),
    path('program-suggestion/', views.program_suggestion, name='program-suggestion'),
    path('programs/program_details/<slug:id>', views.program_details, name='program_details'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/job_details/<slug:id>', views.job_details, name='job_details'),
    path('job-suggestion/', views.job_suggestion, name='job-suggestion'),
    path('visa_information/', views.visa, name='visa_information'),
    path('display_pdf/<slug:pdfname>', views.display_pdf, name='display_pdf'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]