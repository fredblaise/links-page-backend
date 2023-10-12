# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Link, LinkPage


# create a model serializer
class LinkPageSerializer(serializers.HyperlinkedModelSerializer):
    # specify models and fields
    class Meta:
        model = LinkPage
        fields = ("id", "title", "subtitle", "profile_image")


# create a model serializer
class LinkSerializer(serializers.HyperlinkedModelSerializer):
    # specify models and fields
    class Meta:
        model = Link
        fields = ("id", "title", "link", "icon", "color")
