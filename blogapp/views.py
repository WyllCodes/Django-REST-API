
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Post
from .serializers import PostSerializer


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
        