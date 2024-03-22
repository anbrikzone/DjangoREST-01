from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from django.contrib.auth.models import User
from django.forms import model_to_dict

class PostAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all().values()
        return Response({'posts': list(posts)})
    
    def post(self, request):
        user = User.objects.get(id=1)
        post_new = Post.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            author = user
        )
        return Response({
            'message': 'Post created succefully',
            'post': model_to_dict(post_new)
            })
    
    def patch(self, request):
        post = Post.objects.get(id = request.data['post_id'])
        post.title = request.data['title']
        post.content = request.data['content']
        post.save()
        return Response({
            'message': 'Post updated succefully',
            'post': model_to_dict(post)
        })

    def delete(self, request):
        Post.objects.get(id = request.data['post_id']).delete()
        
        posts = Post.objects.all().values()
        return Response({
            'message': 'Post deleted succefully',
            'post': list(posts)
        })