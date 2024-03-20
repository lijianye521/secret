<template>
  <div class="container-fluid" style="min-height: 100vh;">
    <div class="mb-3" style="margin-top: 30px;">
      <label for="formFile" class="form-label">请上传你的数据文件</label>
      <input class="form-control" type="file" id="formFile" ref="file">
      
      <!-- 模型选择下拉菜单 -->
      <select class="form-select mt-3" v-model="selectedModel">
        <option disabled value="">请选择一个模型</option>
        <option value="model1">逻辑回归模型</option>
        <option value="model2">随机森林模型</option>
        <option value="model3">XGBoost模型</option>
      </select>
      
      <div class="container d-flex flex-column justify-content-center align-items-center" style="margin-top: 20px;">
        <button class="btn btn-primary" @click="uploadFile">上传</button>
      </div>
      
      <!-- Bootstrap进度条 -->
      <div v-if="uploadPercentage > 0" class="progress" style="margin-top: 20px;">
        <div class="progress-bar" role="progressbar" :style="{ width: uploadPercentage + '%' }" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">{{ uploadPercentage }}%</div>
      </div>
      
      <!-- 上传成功的消息 -->
      <div v-if="uploadSuccess" class="alert alert-success" style="margin-top: 20px;">
        文件上传成功！
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedModel: '', // 用于存储选中的模型
      uploadPercentage: 0, // 用于存储上传进度的百分比
      uploadSuccess: false, // 用于标识文件是否上传成功
    };
  },
  methods: {
    async uploadFile() {
      this.uploadSuccess = false; // 开始上传时重置上传成功状态
      if (!this.selectedModel) {
        alert('请先选择一个模型');
        return;
      }
      const formData = new FormData();
      const file = this.$refs.file.files[0];
      formData.append("file", file);
      formData.append("model", this.selectedModel); // 将选中的模型添加到表单数据中

      try {
        const response = await axios.post('http://localhost:8000/fileupload/upload/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
          onUploadProgress: progressEvent => {
            // 计算上传进度的百分比并更新uploadPercentage
            this.uploadPercentage = parseInt(Math.round((progressEvent.loaded / progressEvent.total) * 100));
          },
        });
        this.uploadSuccess = true; // 设置上传成功状态
        console.log('File uploaded successfully', response.data);
      } catch (error) {
        this.uploadSuccess = false; // 若有错误，确保上传成功状态为false
        console.error('Error uploading file', error);
      }
    },
  },
};
</script>
