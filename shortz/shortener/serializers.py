from rest_framework import serializers

from .models import URLEntry

class URLEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = URLEntry
        fields = '__all__'
