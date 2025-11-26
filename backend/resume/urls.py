from django.urls import path
from . import views

urlpatterns = [
    path('resumes/', views.ResumeListCreateView.as_view(), name='resume-list'),
    path('resumes/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),
    path('resumes/<int:pk>/export/', views.export_resume_pdf, name='resume-export'),
    
    path('resumes/<int:resume_id>/educations/', views.EducationCreateView.as_view(), name='education-create'),
    path('educations/<int:pk>/', views.EducationDetailView.as_view(), name='education-detail'),
    
    path('resumes/<int:resume_id>/experiences/', views.ExperienceCreateView.as_view(), name='experience-create'),
    path('experiences/<int:pk>/', views.ExperienceDetailView.as_view(), name='experience-detail'),
    
    path('resumes/<int:resume_id>/skills/', views.SkillCreateView.as_view(), name='skill-create'),
    path('skills/<int:pk>/', views.SkillDetailView.as_view(), name='skill-detail'),
    
    path('resumes/<int:resume_id>/projects/', views.ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
]