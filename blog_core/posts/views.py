from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post

class PostAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all().values()
        return Response({'posts': list(posts)})