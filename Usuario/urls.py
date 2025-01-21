#from django.urls import path
#from .views import MembersViewset
#
#urlpatterns = [
#    path('members/<int:pk>', MembersViewset.as_view()),
#    path('members/', MembersViewset.as_view())
#]

from django.urls import path,include
from .views import MembersViewset, SkillViewset, ProjectViewset, PostViewset, SuscriptorViewset
from rest_framework import routers

routers = routers.DefaultRouter()

routers.register('members', MembersViewset, 'members')
routers.register('skill', SkillViewset, 'skill')
routers.register('project', ProjectViewset, 'project')
routers.register('post', PostViewset, 'post')
routers.register('suscriptor', SuscriptorViewset, 'suscriptor')


urlpatterns = [
    path('',include(routers.urls)),
    #path('sendsuscription/',Send_Suscription.as_view())
    #path('members/skill/', SkillViewset.as_view())
]