from django.shortcuts import render
from rest_framework import viewsets,mixins
from . import serializer,models
# Create your views here.




class RegisteredParthersViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = serializer.RegisteredParthersSerilizer
    queryset= models.RegisteredParthers.objects.all()



class ContactViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = serializer.ContactUsSerilizer
    queryset= models.ContactUs.objects.all()
