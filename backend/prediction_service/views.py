from django.http import HttpResponse
import subprocess
import os

def predict(request):
    print(f"当前工作目录: {os.getcwd()}")

    script_path = './prediction_service/model/main.py'
    command = f'python {script_path} --train_file_path ./prediction_service/model/input/internet_service_churn.csv'

    try:
        print("三模型开始预测")
        # 使用 subprocess.Popen 执行命令，并捕获标准输出
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='utf-8')

        # 实时输出
        for line in process.stdout:
            print(line, end="")  # 实时打印输出，也可以按需处理或记录

        process.wait()  # 等待进程结束
        exit_code = process.returncode

        if exit_code == 0:
            print("Script executed successfully")
            return HttpResponse("Script executed successfully.", status=201)
        else:
            print("Script execution failed")
            return HttpResponse("Script execution failed.", status=500)
    except Exception as e:
        print(f"An error occurred: {e}")
        return HttpResponse(f"An error occurred: {e}", status=500)
