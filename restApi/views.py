from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import LinkSerializer, LinkPageSerializer
from .models import Link, LinkPage


# create a viewset
class LinkViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Link.objects.all()

    # specify serializer to be used
    serializer_class = LinkSerializer


class LinkPageViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = LinkPage.objects.all()

    # specify serializer to be used
    serializer_class = LinkPageSerializer
