from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    """
       Serializer class for Blog
    """
    mage_path = serializers.CharField(required=False, default=None)
    title = serializers.CharField(required=True)
    body = serializers.CharField(required=True)
    
    class Meta:
        model = Blog
        fields = ('mage_path', 'id', 'created_at', 'updated_at', 'title',
                  'body')

        read_only_fields = ('id',
                            'created_at', 'updated_at')