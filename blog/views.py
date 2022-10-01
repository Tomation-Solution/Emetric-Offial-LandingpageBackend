from django.shortcuts import render

from . import models,serializer,filter
from rest_framework import mixins,viewsets


class BlogViewSets(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class = serializer.BlogSerializer
    queryset= models.BlogPost.objects.all()

    filterset_class = filter.BlogFilter