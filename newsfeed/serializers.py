from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Newsfeed

class NewsfeedSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Newsfeed
        fields = ('title', 'content', 'image')