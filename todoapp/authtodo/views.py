from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from authtodo.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import authentication, permissions


"""
from rest_framework import authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class ListUsers(APIView):
    
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        
        Return a list of all users.
        
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)




class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

"""


class RegisterUser(APIView):
    authentication_classes = []
    permission_classes = []


    def post(self, request):
        serializer = UserSerializer(data = request.data)
        
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
        
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user = user)
        return Response({'status': 200, 'payload': serializer.data,'token': str(token_obj), 'message': 'Your data is saved'})
    
    
    
    ######################
from django.shortcuts import render
from rest_framework import viewsets
from authtodo.serializers import TodoSerializer
from .models import Todo

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer