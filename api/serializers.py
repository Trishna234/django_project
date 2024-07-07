from rest_framework import serializers  # convert python object into json object

from base.models import ToDo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'content', 'is_completed', 'created_at', 'updated_at']


