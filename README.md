# Django REST API (DJANGO REST_FRAMEWORK)

This tutorial will teach you about Django REST API using the Django Rest Frame Work.

## Getting Started

### 1. Setting up a Django Project

- Create and enter the desired directory for project setup I’m using blogapi.

- Create a virtual environment using python -m venv venv or try pipenv :

    ``` shell
    pip install pipenv
    pipenv shell
    ```

- pipenv de-activation and re-activation

- Install Django:

    ```shell
    pip install django
    ```

- Create a Django project called blogapiproj:

    ```shell
    django-admin startproject blogapiproj
    ```

- Create an app called blogapp:

    ```shell
    python manage.py startapp blogapp
    ```

- Open the project in your code editor.


- Register the app in the project's INSTALLED_APPS in 
settings.py file.

- Create URLs for the blogapp and register them in the project's URLs.

### 6. Making required imports

- Head to your views.py file and import the following:

  ```
  python
  from django.shortcuts import render
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  from .models import Post
  from .serializers import PostSerializer 

*
    ```


### 7. Creating GET, POST, PUT & DELETE Views

# Create your views here.
    @api_view(['GET'])
    def index(request):
    
    return Response({"Success": "They API setup was Succesfull"})
    
#VIEW TO GET ALL POST ON THE API
       
    @api_view(['GET'])
    def GetAllPosts(request):
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True)
    
    return Response(serializer.data)

    @api_view(['GET', 'POST'])
    def CreatePost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success:" "The post was Created Successfully"}, status=201)  
    else:
        return Response(serializer.errors, status=400)  
    
# VIEW TO DELETE A POST FROM THEY API
    @api_view(['DELETE'])
    def DeletePost(request):
    post_id = request.data.get('post_id')
    try:
        Post = Post.objects.get(id=post_id)
        Post.delete()
        return Response({"Success": "The Post was Successfully Deleted"})
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)
    
    
    
# VIEW TO RETRIEVE POST BY POST_id
    @api_view(['GET'])
        def GetPost(request):
    post_id =request.data.get('post_id')
    try:
        Post = Post.objects.get(id=post_id)
        Serializer = PostSerializer(Post)
        return Response(Post)
      except:
        return Response({"Error": " The post does not exist"}, status=404)
    
    
# VIEW TO CREATE A NEW POST ON THEY BLOG
    @api_view(['PUT'])
    def UpdatePost(request):
    post_id = request.data.get('post_id')
    get_new_title = request.data.get('new_title')
    get_new_content = request.data.get('new_content')
    
    try:
        Post = Post.objects.get(id=post_id)
        
        if get_new_title:
            Post.title = get_new_title
        if get_new_content:
            Post.content = get_new_content
            
        Post.save()
        return Response({"Sucess": "The Post was Successfully Updated!!"}, status=201)
    
    except Post.DoesNotExist:
        return Response({"Error":" The Post Does not Exist"}, status=404)
        

- Map views to urls:

```
    urlpatterns = [
    path('', views.index),
    path('get-all-posts/', views.GetAllPosts),
    path('create-new-post/', views.CreatePost),
    path('delete-post/', views.DeletePost),
    path('get-post/', views.GetPost),
    path('update-posts/', views.UpdatePost),

    ]

```

### 8. Working on the models.py file

       ``` 
    from django.db import models
 # Create your models here.
    class Post(models.Model):
               title = models.CharField(max_length=200)
              content = models.TextField()
             def __str__(self):
        return self.title

    ```
        

### 9. Working on the serializer to convert data to JSON type, copy to your serializers.py file
    
    ```  
     from rest_framework.serializers import ModelSerializer
     from .models import Post

    class PostSerializer(ModelSerializer):
          class Meta:
          model = Post
        fields = '__all__'
        
     ```
### 10. Register your models in the admin site, in your models.py file

    ```  
        from django.contrib import admin
       from .import models

   # Register your models here.
      admin.site.register(models.Post)

    ```

### 11. Test The Code using Postman an API testing tool(software)




