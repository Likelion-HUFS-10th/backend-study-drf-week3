from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer, BlogCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
'''
전체 블로그를 조회
'''
@api_view(['GET'])
def get_all_blogs(request):
    # authentication
    blogs = Blog.objects.all()
    for blog in blogs:
        print("제목",blog.title)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

'''
한 블로그 post
'''
@api_view(['POST'])
def post_one_blog(request):
    serializer = BlogCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

'''
한 블로그 조회
'''
@api_view(['GET'])
def get_one_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

'''
한 블로그 수정
'''
@api_view(['PUT'])
def put_one_blog(request, pk):
    try: 
        blog = Blog.objects.get(pk=pk)
        serializer = BlogCreateSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

'''
한 블로그 삭제
'''
@api_view(['DELETE'])
def delete_one_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)