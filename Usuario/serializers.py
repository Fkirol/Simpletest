from rest_framework import serializers
from .models import Member, Skill, Project, Post , Suscriptor


class SuggestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "author", "title", "seo_title", "content", "status", "date_time")

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        
class ProjectSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Project
        fields = ("id","name","featured_image","description","url","skills")
        
    
    def get_skills(self, instance):
        
        return SkillSerializer(instance.skills.all(), many=True).data      

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'        
        
class SkillMembersSerializer(serializers.ModelSerializer):
    skill = serializers.SerializerMethodField(read_only=True)
    members = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Skill
        fields = ('skill','members')
        
    def get_skill(self,instance):
        serializer = SkillSerializer(instance)
    
        return serializer.data
        
    def get_members(self,instance):    
        return Member.objects.filter(skills=instance).values('username','profile_picture')
    

class PostSerializer(serializers.ModelSerializer):
    suggest = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Post
        fields = ("id", "author", "title", "seo_title", "content", "status", "date_time","suggest")

    def get_suggest(self, instance):
        
        return SuggestSerializer(instance.suggests.all(), many=True).data

class SuscriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscriptor
        fields = ['email']
    
