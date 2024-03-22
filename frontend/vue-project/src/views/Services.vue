<template>
  <div class="container-fluid" style="min-height: 100vh;">
    <div class="mb-3" style="margin-top: 30px;">
      <label for="formFile" class="form-label">请上传你的数据文件</label>
      <input class="form-control" type="file" id="formFile" ref="file">
      
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
import { uploadFile } from '@/api/api'; // 假设api文件在src目录下

export default {
  data() {
    return {
      uploadPercentage: 0, // 用于存储上传进度的百分比
      uploadSuccess: false, // 用于标识文件是否上传成功
    };
  },
  methods: {
    async uploadFile() {
      this.uploadSuccess = false; // 开始上传时重置上传成功状态
      const formData = new FormData();
      const file = this.$refs.file.files[0];
      formData.append("file", file);

      try {
        const response = await uploadFile(formData, progressEvent => {
          // 计算上传进度的百分比并更新uploadPercentage
          this.uploadPercentage = parseInt(Math.round((progressEvent.loaded / progressEvent.total) * 100));
        });
        this.uploadSuccess = true; // 设置上传成功状态
        console.log('File uploaded successfully', response);
      } catch (error) {
        this.uploadSuccess = false; // 若有错误，确保上传成功状态为false
        console.error('Error uploading file', error);
      }
    },
  },
};
</script>
