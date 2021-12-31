from rest_framework import serializers
from .models import File, Work

class FileSerializer(serializers.ModelSerializer):
    filename = serializers.CharField(max_length=200)
    work_count = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = File
        fields = ('__all__')

class WorkSerializer(serializers.ModelSerializer):
    file_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    contributors = serializers.CharField(max_length=200)
    iswc = serializers.CharField(max_length=200)
    source = serializers.CharField(max_length=200)
    proprietary_id = serializers.IntegerField()

    class Meta:
        model = Work
        fields = ('__all__')
