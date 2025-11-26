from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Resume, Education, Experience, Skill, Project
from .serializers import *

class ResumeListCreateView(generics.ListCreateAPIView):
    serializer_class = ResumeListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

class EducationCreateView(generics.CreateAPIView):
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        resume = get_object_or_404(Resume, id=self.kwargs['resume_id'], user=self.request.user)
        serializer.save(resume=resume)

class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Education.objects.filter(resume__user=self.request.user)

class ExperienceCreateView(generics.CreateAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        resume = get_object_or_404(Resume, id=self.kwargs['resume_id'], user=self.request.user)
        serializer.save(resume=resume)

class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Experience.objects.filter(resume__user=self.request.user)

class SkillCreateView(generics.CreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        resume = get_object_or_404(Resume, id=self.kwargs['resume_id'], user=self.request.user)
        serializer.save(resume=resume)

class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Skill.objects.filter(resume__user=self.request.user)

class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        resume = get_object_or_404(Resume, id=self.kwargs['resume_id'], user=self.request.user)
        serializer.save(resume=resume)

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(resume__user=self.request.user)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def export_resume_pdf(request, pk):
    # This would integrate with a PDF generation library like WeasyPrint or ReportLab
    # For now, return JSON data that can be used by frontend to generate PDF
    resume = get_object_or_404(Resume, id=pk, user=request.user)
    serializer = ResumeSerializer(resume)
    return Response(serializer.data)