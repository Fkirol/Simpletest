from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import  ListAPIView, CreateAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from .serializers import MemberSerializer , SkillMembersSerializer, ProjectSerializer, PostSerializer, SuscriptorSerializer, SuscribeSerializer
from .models import Member, Skill, Project, Post as Postdb, Suscriptor
from rest_framework.response import Response
from django.core.mail import send_mail
import os
    
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
    

    def post(self, request, *args, **kwargs):
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            message = request.data.get('message')
            please_suscribe = request.data.get('please_suscribe')
            
            please_suscribe = bool(please_suscribe)
          
            suscribe="No Suscribed"
            if Suscriptor.objects.filter(email=email).exists():
                
                if please_suscribe==False:
                    suscribe="Suscribed"
                else:
                    suscribe="Suscribe"
            else:
                if please_suscribe==True:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    suscribe="Suscribed"

            
            send_mail(
            f"Hola, {name}",
            f"{email} {suscribe} {message}",
            "bryanayala080808@gmail.com",
            ["kirolukushi@gmail.com","martinezotano972@gmail.com"],
            fail_silently=True,
            )
            return Response({"Success":"El mensaje fue enviado con exito"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":f"Ocurrio un error: {e}"},status=status.HTTP_408_REQUEST_TIMEOUT)
         
    
class SuscribeViewset(CreateAPIView,GenericViewSet):
    serializer_class = SuscribeSerializer
    def create(self, request, *args, **kwargs): 
        try:
            email = request.data.get('email')
            if Suscriptor.objects.filter(email=email).exists():
                return Response({"Status":"Suscribed"},status=status.HTTP_200_OK)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save() 
            send_mail(
            "Hola",
            "Gracias por Suscribirte",
            "bryanayala080808@gmail.com",
            ["kirolukushi@gmail.com"],
            fail_silently=True,
            )
            return Response({"Status":"Done"},status=status.HTTP_200_OK) 
        except Exception as e:
                return Response({"error":f"Ocurrio un error: {e}"},status=status.HTTP_408_REQUEST_TIMEOUT)
          
                   
        
        

                
                


    
    
