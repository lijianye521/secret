from django.shortcuts import render
# fileupload/views.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        # 你可以在这里处理文件，比如保存到服务器的某个位置
        return Response({'message': 'File has been uploaded successfully!'}, status=status.HTTP_201_CREATED)
