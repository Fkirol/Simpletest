import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Proyecto.settings")
django.setup()

from Usuario.models import Member, Post


from django.contrib.auth.hashers import make_password 
from django.contrib.auth import get_user_model
from Usuario.models import Skill, Member, Project, Post, Suscriptor  # Reemplaza 'app' con tu app
from Usuario.utils import scrape_pinterest_board

User = get_user_model() # Obten el modelo de usuario configurado
def create_skills():
    skills_data = [
        {"skill_name": "Python", "skill_description": "Programming language"},
        {"skill_name": "JavaScript", "skill_description": "Web scripting language"},
        {"skill_name": "Django", "skill_description": "Web framework"},
        {"skill_name": "React", "skill_description": "JavaScript library for user interfaces"},
        {"skill_name": "Docker", "skill_description": "Containerization platform"},
        {"skill_name": "SQL", "skill_description": "Database language"},
        {"skill_name": "HTML", "skill_description": "Markup language"},
        {"skill_name": "CSS", "skill_description": "Style sheet language"},
        {"skill_name": "Git", "skill_description": "Version control system"},
        {"skill_name": "AWS", "skill_description": "Cloud services"},
    ]
    skills = []
    for data in skills_data:
        skill = Skill.objects.create(**data)
        skills.append(skill)
    return skills


def create_members(skills):
    members_data = [
        {
            "username": "john_doe",
            "password": "password123",  # Usar make_password para hashear
            "presentation": "Software developer with experience in Python and Django",
            "phone_number": "555-1234",
            "skills": [skills[0],skills[2],skills[5]]  # Skills Python,Django,SQL
        },
         {
            "username": "jane_smith",
            "password": "securepass",  # Usar make_password para hashear
            "presentation": "Frontend developer specializing in React",
            "phone_number": "555-5678",
             "skills": [skills[1],skills[3],skills[7]]   #Skills Javascript,React,CSS
         },
         {
             "username": "peter_jones",
            "password": "mypassword",  # Usar make_password para hashear
            "presentation": "System administrator with experience in Docker and AWS",
             "phone_number": "555-9012",
             "skills": [skills[4],skills[9],skills[5]]  #Skills Docker,AWS,SQL
        },
        {
            "username": "lisa_brown",
            "password": "lisa123",  # Usar make_password para hashear
            "presentation": "Web designer with expertise in HTML and CSS",
            "phone_number": "555-3456",
            "skills": [skills[6], skills[7]] #Skills HTML,CSS
         },
        {
            "username": "mike_williams",
             "password": "secure123",  # Usar make_password para hashear
             "presentation": "Data scientist with experience in SQL and Python",
            "phone_number": "555-7890",
             "skills": [skills[0],skills[5]]  #Skills Python,SQL
         },
        {
            "username": "sarah_miller",
            "password": "sarah123",  # Usar make_password para hashear
            "presentation": "Fullstack developer with knowledge in Django and React",
            "phone_number": "555-2345",
            "skills": [skills[2], skills[3]] #Skills Django,React
          },
        {
            "username": "david_garcia",
            "password": "david123",  # Usar make_password para hashear
            "presentation": "Software engineer with experience in Git and Python",
            "phone_number": "555-6789",
           "skills": [skills[0],skills[8]]  #Skills Python,Git
         },
        {
            "username": "emily_davis",
            "password": "emily123",  # Usar make_password para hashear
            "presentation": "Cloud engineer specializing in AWS",
            "phone_number": "555-0123",
            "skills": [skills[9],skills[4]]   #Skills AWS,Docker
        },
        {
             "username": "brian_anderson",
             "password": "brian123",  # Usar make_password para hashear
            "presentation": "Database administrator with expertise in SQL",
             "phone_number": "555-4567",
             "skills": [skills[5]]  #Skills SQL
         },
          {
              "username": "olivia_martinez",
             "password": "olivia123",  # Usar make_password para hashear
             "presentation": "Web developer with skills in JavaScript, HTML, and CSS",
             "phone_number": "555-8901",
             "skills": [skills[1], skills[6], skills[7]]  #Skills Javascript,HTML,CSS
        },
     ]
    members = []
    scraped_images = scrape_pinterest_board("https://es.pinterest.com/ideas/")
    if not scraped_images:
        print("No se pudieron obtener imágenes de Pinterest, asegurate de que la URL es valida")
        return []

    for i, data in enumerate(members_data):
        skills = data.pop('skills') #pop para extraer las skills del diccionario
        password = make_password(data.pop('password'))

        #Asignar imagen si hay disponible
        image_url = scraped_images[i % len(scraped_images)]['image'] if i < len(scraped_images) else 'default.jpg'

        member = Member.objects.create(**data,password=password,profile_picture=image_url)
        member.skills.set(skills) # Usamos set para agregar la lista de skills
        members.append(member)
    return members




def create_projects(skills):
    projects_data = [
         {
            "name": "E-commerce Platform",
            "description": "Web platform for online shopping",
            "url": "https://ecommerce.example.com",
            "skills": [skills[0], skills[2], skills[6], skills[7]] #Python, Django, HTML, CSS
        },
        {
            "name": "Task Management App",
            "description": "Application for managing tasks and projects",
            "url": "https://taskmanager.example.com",
           "skills": [skills[1], skills[3], skills[5]] #JavaScript, React, SQL
         },
        {
            "name": "Blog Website",
            "description": "A simple blog website",
             "url": "https://blog.example.com",
            "skills": [skills[0],skills[2], skills[6]] #Python, Django, HTML
          },
        {
            "name": "Portfolio Website",
            "description": "Website for showcasing a personal portfolio",
           "url": "https://portfolio.example.com",
            "skills": [skills[1], skills[6], skills[7]] #JavaScript, HTML, CSS
         },
         {
             "name": "Weather App",
            "description": "Application for getting weather information",
             "url": "https://weatherapp.example.com",
             "skills": [skills[1], skills[3]] #JavaScript, React
        },
        {
            "name": "Inventory System",
            "description": "System for managing inventory of products",
             "url": "https://inventory.example.com",
            "skills": [skills[0], skills[2], skills[5]] #Python, Django, SQL
        },
        {
            "name": "Social Media Platform",
            "description": "Platform for social interactions",
            "url": "https://socialmedia.example.com",
            "skills": [skills[1], skills[3], skills[6], skills[7]] #JavaScript, React, HTML, CSS
         },
        {
           "name": "Document Management System",
            "description": "System for managing and organizing documents",
            "url": "https://documentmanager.example.com",
           "skills": [skills[0], skills[4],skills[5]] #Python, Docker, SQL
         },
        {
            "name": "Cloud Deployment Platform",
            "description": "Platform for deploying applications to the cloud",
            "url": "https://cloud.example.com",
             "skills": [skills[4], skills[9]] #Docker, AWS
          },
         {
             "name": "Real-Time Chat Application",
            "description": "Application for real-time messaging",
            "url": "https://chat.example.com",
           "skills": [skills[1], skills[3]] #JavaScript, React
        },
    ]
    projects = []
    scraped_images = scrape_pinterest_board("https://es.pinterest.com/ideas/")
    if not scraped_images:
        print("No se pudieron obtener imágenes de Pinterest, asegurate de que la URL es valida")
        return []
    for i,data in enumerate(projects_data):
      skills_data = data.pop('skills') #pop para extraer las skills del diccionario
      image_url = scraped_images[i % len(scraped_images)]['image'] if i < len(scraped_images) else 'default.jpg'
      project = Project.objects.create(**data,featured_image=image_url)
      project.skills.set(skills_data) # Usamos set para agregar la lista de skills
      projects.append(project)
    return projects

def create_posts(members):
    posts_data = [
         {
            "author": members[0],
            "title": "First Steps with Django",
            "seo_title": "first-steps-with-django",
            "content": "This is the first article about Django.",
            "featured_image": "https://www.instagram.com/waifu_posting_hololive/p/CdTuKP2u6Fl/",
              "suggests": [],
             "status": Post.Status.PUBLISHED
        },
        {
             "author": members[1],
            "title": "Introduction to React",
            "seo_title": "introduction-to-react",
             "content": "This is an introductory article about React.",
             "featured_image": "https://co.pinterest.com/pin/monas-chinas-animes-por-cierto-u--622833823471593702/",
             "suggests": [],
            "status": Post.Status.PUBLISHED
        },
         {
             "author": members[2],
             "title": "Docker for Beginners",
             "seo_title": "docker-for-beginners",
             "content": "This post introduces Docker concepts.",
             "featured_image": "https://www.threads.net/@lsamir2425l/post/CukaUlaxp4M",
             "suggests": [],
            "status": Post.Status.PUBLISHED
         },
        {
             "author": members[3],
            "title": "Styling with CSS",
            "seo_title": "styling-with-css",
            "content": "This article focuses on styling web pages with CSS.",
             "featured_image": "https://www.reddit.com/r/Genshin_Impact/comments/101gaou/raiden_shogun_art_by_me/?rdt=34605",
              "suggests": [],
              "status": Post.Status.PUBLISHED
         },
        {
            "author": members[4],
            "title": "Advanced Python Techniques",
             "seo_title": "advanced-python-techniques",
            "content": "This post covers advanced Python techniques.",
             "featured_image": "https://www.hoyolab.com/article/31310760",
             "suggests": [],
             "status": Post.Status.PUBLISHED
        },
       {
            "author": members[5],
             "title": "Building a Fullstack App with Django and React",
            "seo_title": "fullstack-django-react",
            "content": "This article explains how to combine Django and React.",
             "featured_image": "https://bishoujocomplex.com/products/raiden-shogun-casual-g14",
             "suggests": [],
            "status": Post.Status.PUBLISHED
         },
         {
              "author": members[6],
            "title": "Git Workflow",
            "seo_title": "git-workflow",
            "content": "This post focuses on Git workflow strategies.",
             "featured_image": "https://co.pinterest.com/pin/monas-chinas-animes-por-cierto-u--622833823471593702/",
           "suggests": [],
            "status": Post.Status.PUBLISHED
         },
        {
           "author": members[7],
            "title": "AWS Basics",
             "seo_title": "aws-basics",
            "content": "This post is a guide to basic AWS concepts.",
             "featured_image": "https://co.pinterest.com/pin/monas-chinas-animes-por-cierto-u--622833823471593702/",
             "suggests": [],
            "status": Post.Status.PUBLISHED
          },
        {
              "author": members[8],
             "title": "SQL Queries",
            "seo_title": "sql-queries",
             "content": "This is an article about basic SQL queries.",
             "featured_image": "https://co.pinterest.com/pin/monas-chinas-animes-por-cierto-u--622833823471593702/",
              "suggests": [],
              "status": Post.Status.PUBLISHED
          },
         {
            "author": members[9],
            "title": "Web Development Basics",
            "seo_title": "web-development-basics",
           "content": "This article is for the beginners in web development.",
             "featured_image": "https://co.pinterest.com/pin/monas-chinas-animes-por-cierto-u--622833823471593702/",
           "suggests": [],
           "status": Post.Status.PUBLISHED
         }

    ]
    posts = []
    for data in posts_data:
        suggested_posts = data.pop('suggests')
        post = Post.objects.create(**data)
        post.suggests.set(suggested_posts)
        posts.append(post)

    for i, post in enumerate(posts):
       if i < len(posts)-1: # Si no es el ultimo post, le sugerimos el siguiente
         post.suggests.add(posts[i+1])

    return posts



def create_suscriptors():
     suscriptors_data = [
        {"email": "subscriber1@example.com"},
        {"email": "subscriber2@example.com"},
        {"email": "subscriber3@example.com"},
        {"email": "subscriber4@example.com"},
        {"email": "subscriber5@example.com"},
        {"email": "subscriber6@example.com"},
        {"email": "subscriber7@example.com"},
        {"email": "subscriber8@example.com"},
        {"email": "subscriber9@example.com"},
        {"email": "subscriber10@example.com"},
    ]

     suscriptors = []
     for data in suscriptors_data:
         suscriptor = Suscriptor.objects.create(**data)
         suscriptors.append(suscriptor)

     return suscriptors





def delete_all_data():
    print("Deleting all data...")

    # Eliminar todos los registros de Skill
    num_skills_deleted, _ = Skill.objects.all().delete()
    print(f"Deleted {num_skills_deleted} Skills.")

    # Eliminar todos los registros de Member
    num_members_deleted, _ = Member.objects.all().delete()
    print(f"Deleted {num_members_deleted} Members.")

    # Eliminar todos los registros de Project
    num_projects_deleted, _ = Project.objects.all().delete()
    print(f"Deleted {num_projects_deleted} Projects.")

    # Eliminar todos los registros de Post
    num_posts_deleted, _ = Post.objects.all().delete()
    print(f"Deleted {num_posts_deleted} Posts.")

    # Eliminar todos los registros de Suscriptor
    num_suscriptors_deleted, _ = Suscriptor.objects.all().delete()
    print(f"Deleted {num_suscriptors_deleted} Suscriptors.")


try:
    Member.objects.get('admin')
except:
    delete_all_data()
    Member.objects.create_superuser(
        username="admin",
        password="admin",
        profile_picture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFiXgfcBgdIhvWXh0KJcIypUIGJ_x1-dGOOQ&s"
    )
    print("Creating Skills...")
    skills = create_skills()

    print("Creating Members...")
    members = create_members(skills)

    print("Creating Projects...")
    projects = create_projects(skills)

    print("Creating Posts...")
    posts = create_posts(members)
    print("Creating Suscriptors...")
    suscriptors = create_suscriptors()

    print("Data creation complete.")
