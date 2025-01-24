from rest_framework import serializers
from .models import Member, Skill, Project, Post , Suscriptor


class SuggestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "author", "title", "seo_title","status", "date_time","featured_image")

class MemberSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Member
        fields = ("id","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined","presentation","profile_picture","phone_number","groups","user_permissions","skills")
    
    def get_skills(self,instance):
            return SkillSerializer(instance.skills.all(), many=True).data
        
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
        fields = ("id", "author", "title", "seo_title", "content", "status", "date_time","featured_image","suggest")

    def get_suggest(self, instance):
        
        return SuggestSerializer(instance.suggests.all(), many=True).data

class SuscriptorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200,write_only=True,required=True,allow_blank=False)
    message = serializers.CharField(max_length=200,write_only=True,required=True,allow_blank=False)
    email = serializers.EmailField(max_length=200)
    please_suscribe = serializers.BooleanField(write_only=True)
    
    def create(self, validated_data):
        validated_data.pop("name")
        validated_data.pop("message")
        validated_data.pop("please_suscribe")
        return super().create(validated_data) 
    
    class Meta:
        model = Suscriptor
        fields = "__all__"
        
class SuscribeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100,required=True,allow_blank=False)
    class Meta:
        model = Suscriptor
        fields = ['email']
        
