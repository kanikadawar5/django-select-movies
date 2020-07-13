from rest_framework import serializers

from .models import Values


class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Values
        fields = ('request_id', 'movies', 'create_time')
        read_only_field = None
