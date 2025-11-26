from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Resume(models.Model):
    TEMPLATE_CHOICES = [
        ('modern', 'Modern'),
        ('classic', 'Classic'),
        ('creative', 'Creative'),
        ('professional', 'Professional'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    template = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, default='modern')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)
    
    # Professional Summary
    summary = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"

class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='educations', on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experiences', on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class Skill(models.Model):
    resume = models.ForeignKey(Resume, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert')
    ])
    
    def __str__(self):
        return self.name

class Project(models.Model):
    resume = models.ForeignKey(Resume, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    project_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name