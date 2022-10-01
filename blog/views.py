from django.shortcuts import render

from . import models,serializer
from rest_framework import mixins,viewsets

class BlogViewSets(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = serializer.BlogSerializer
    queryset= models.BlogPost.objects.all()
    