from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class Skill(models.Model):
    skill_name = models.CharField(max_length=200, default=None)
    skill_description = models.CharField(max_length=200, default=None)
    def __str__(self):
        return self.skill_name


class Member(AbstractUser):
    presentation = models.TextField(null=True)
    profile_picture = models.CharField(max_length=200, default=None,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    skills = models.ManyToManyField(Skill)
   
    
class Project(models.Model):
    name = models.TextField()
    featured_image = models.CharField(max_length=200,default=None)
    description = models.CharField(max_length=200,default=None)
    url = models.CharField(max_length=200,default=None)
    skills = models.ManyToManyField(Skill)
    def __str__(self):
        return self.name

    
class Post(models.Model):
    class Status(models.IntegerChoices):
        UNPUBLISHED = 0, 'Borrador'
        PUBLISHED = 1, 'Publicado'
        

        
    author = models.ForeignKey(Member,on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=200,default=None)
    seo_title  = models.CharField(max_length=200,default=None,unique=True)
    content = models.TextField()
    suggests = models.ManyToManyField('self', symmetrical=False, blank=True)
    status = models.IntegerField(choices=Status.choices, default=Status.UNPUBLISHED)
    date_time = models.DateTimeField(auto_now_add=True)
    


class Suscriptor(models.Model):
    email = models.EmailField(max_length=200,unique=True,default=None)