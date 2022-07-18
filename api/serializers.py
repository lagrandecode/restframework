
from rest_framework import serializers
from .models import Api

class Apiserializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ['name','title','Address']