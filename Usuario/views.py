from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import  ListAPIView, CreateAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from .serializers import MemberSerializer , SkillMembersSerializer, ProjectSerializer, PostSerializer, SuscriptorSerializer, SuscribeSerializer, PinterestImageSerializer
from .models import Member, Skill, Project, Post as Postdb, Suscriptor
from rest_framework.response import Response
from django.core.mail import send_mail
import os
from . import utils
from django.db.models import Q
    
class MembersViewset(ReadOnlyModelViewSet):
    serializer_class = MemberSerializer
    queryset =  Member.objects.all()  
    
class SkillViewset(ListAPIView,GenericViewSet):
    serializer_class = SkillMembersSerializer
    queryset = Skill.objects.all()
    
class ProjectViewset(ListAPIView,GenericViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            return Project.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return Project.objects.all()
    
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
    

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            name = request.data.get('name')
            email = request.data.get('email')
            message = request.data.get('message')
            please_suscribe = request.data.get('please_suscribe')
            serializer = self.get_serializer(data=request.data)
            
            please_suscribe = bool(please_suscribe)
          
            if please_suscribe==False:
                suscribe="Not Suscribed"
            else:
                suscribe="Suscribed"
                serializer.is_valid(raise_exception=True)
                serializer.save()
                suscribe="Suscribed"

            
            send_mail(
            f"Hello, {name}",
            f"This is your email:{email},                Status:{suscribe}                    Message:{message}",
            "codeslayersdevs@gmail.com",
            [f"{email}"],
            fail_silently=True,
            )
            return Response({"Success":"El mensaje fue enviado con exito"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":f"Ocurrio un error: {e}"},status=status.HTTP_408_REQUEST_TIMEOUT)
         
    
class SuscribeViewset(CreateAPIView,GenericViewSet):
    serializer_class = SuscribeSerializer
    def create(self, request): 
        try:
            email = request.data.get('email')
            if Suscriptor.objects.filter(email=email).exists():
                return Response({"Status":"Suscribed"},status=status.HTTP_200_OK)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save() 
            
            send_mail(
            "Hello there",
            "We're glad to have you on board!",
            "codeslayersdevs@gmail.com",
            [f'{email}'],
            fail_silently=True,
            )
            return Response({"Status":"Done"},status=status.HTTP_200_OK) 
        except Exception as e:
                return Response({"error":f"Ocurrio un error: {e}"},status=status.HTTP_408_REQUEST_TIMEOUT)
            
class PinterestScraperView(APIView):
    serializer_class = PinterestImageSerializer
    def post(self, request):
        board_url = request.data.get('board_url')
        print(board_url)
        if not board_url:
            return Response({'error': 'Se requiere la URL del tablero.'}, status=status.HTTP_400_BAD_REQUEST)

        scraped_data = utils.scrape_pinterest_board(board_url)
        #print(scraped_data)
        if scraped_data is None:
            return Response({'error': 'Error al hacer scraping en el tablero'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = PinterestImageSerializer(data=scraped_data, many=True)
        if serializer.is_valid():
            return Response(scraped_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

                   
        
        

                
                


    
    
