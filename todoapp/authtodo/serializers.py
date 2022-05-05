from django.contrib.auth.models import User
from rest_framework import serializers
#from django.contrib.auth.password_validation import validate_password


#class UserSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = User
   #     fields = ['url', 'username', 'email']
        
        
#class RegistrationSerializer(serializers.ModelSerializer):
    
 #   class Meta:
  #      model = User
   #     fields = [
    #        "Email_Address",
     #       "password",]
      #  extra_kwargs = {'password': {'write_only': True}}
        
        
    #def create(self, validated_data):
     #   user = User(
      #      email=validated_data['email'],
       #     username=validated_data['username']
        #)
        #extra_kwargs = {"password": {"write_only": True}}
        #user = User.objects.create_user(
         #   email=validated_data['email']
        #)
        #password = self.validated_data["password"]
        #account.set_password(password)
        #account.save()
        #return account

        #user.set_password(validated_data['password'])
        #user.save()
        #return user
        
        
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username','password']
    
    
    
###################
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
