from rest_framework import serializers 
from .models import demo

class demoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = demo 
        fields = '__all__' 
