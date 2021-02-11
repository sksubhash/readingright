from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from . import serializers
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Post
from rest_framework import status
from django.contrib.auth.models import User


#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request,):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


#POST API
class PostApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        restaurants = Post.objects.all()
        serializer = serializers.PostSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.PostSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserApi(generics.GenericAPIView):
    def get(self, request):
        restaurants = User.objects.all()
        serializer = serializers.UserSerializer(restaurants, many=True)
        return Response(serializer.data)

