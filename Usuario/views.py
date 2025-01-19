from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView, CreateAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from .serializers import MemberSerializer , SkillMembersSerializer, ProjectSerializer, PostSerializer, SuscriptorSerializer
from .models import Member, Skill, Project, Post as Postdb, Suscriptor
from rest_framework.response import Response

class MembersViewset(ReadOnlyModelViewSet):
    serializer_class = MemberSerializer
    queryset =  Member.objects.all()  
    
class SkillViewset(ListAPIView,GenericViewSet):
    serializer_class = SkillMembersSerializer
    queryset = Skill.objects.all()
    
class ProjectViewset(ListAPIView,GenericViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    
class PostViewset(ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Postdb.objects.all()
    

    def list(self, request, *args, **kwargs):
        self.queryset = Postdb.objects.filter(status=1)
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        
        if kwargs["pk"]:
            
            try:
                int(kwargs["pk"])
                return super().retrieve(request, *args, **kwargs)
            
            except ValueError:
                instance = Postdb.objects.filter(seo_title=kwargs["pk"]).first() 
                serializer = self.get_serializer(instance)
                return Response(serializer.data)

class SuscriptorViewset(CreateAPIView, GenericViewSet):
    serializer_class = SuscriptorSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')

        if Suscriptor.objects.filter(email=email).exists():
            return Response({"status": "subscribed"}, status=status.HTTP_200_OK)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "done"}, status=status.HTTP_201_CREATED)
    

                
                
                


    
    
