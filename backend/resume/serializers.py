from rest_framework import serializers
from .models import Resume, Education, Experience, Skill, Project

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Resume
        fields = '__all__'
        read_only_fields = ('user',)

class ResumeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'title', 'template', 'created_at', 'updated_at')