from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer, WorkSerializer
from .models import File, Work
import pandas as pd
import json

# Create your views here.
class FileViews(APIView):
    def post(self, request):
        serializer = FileSerializer(data=request.data)
        data = request.data
        if serializer.is_valid():
            serializer.save()
            df = pd.read_csv("/code/files/{}".format(data['filename']))
            df['file_id'] = serializer.data['id']
            work_data = df.to_dict(orient='records')
            
            for work in work_data:

                Work.objects.create(**work)

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = File.objects.get(id=id)
            serializer = FileSerializer(item)
            return Response({"status": "success", "file": serializer.data}, status=status.HTTP_200_OK)

        items = File.objects.all()
        serializer = FileSerializer(items, many=True)
        return Response({"status": "success", "file": serializer.data}, status=status.HTTP_200_OK)


class FileDataViews(APIView):
    def get(self, request, file_id=None, id=None):
        items = Work.objects.all()

        serializer = WorkSerializer(items, many=True)
        if file_id and id:
            return Response({"status": "success", "work":  list(filter(lambda x: (x['file_id'] == file_id) and (x['id'] == id), serializer.data))}, status=status.HTTP_200_OK)
 
        if not id:
            
            return Response({"status": "success", "work":  list(filter(lambda x: x['file_id'] == file_id, serializer.data))}, status=status.HTTP_200_OK)

            
