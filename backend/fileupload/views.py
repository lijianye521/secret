import os
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# 你的目标文件夹
save_dir = 'files'

# 检查目标文件夹是否存在，如果不存在则创建
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.data.get('file')  # 获取上传的文件对象
        model_choice = request.data.get('model')  # 获取模型选择

        if file_obj:  # 确保有文件被上传
            # 定义文件的保存路径
            save_path = os.path.join('files', file_obj.name)
            # 打开指定路径的文件以写入上传的文件内容
            with open(save_path, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)

        return Response(data={"message": "文件上传成功，选择的模型是：" + model_choice}, status=status.HTTP_201_CREATED)
