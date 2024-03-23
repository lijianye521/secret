<template>
  <div class="container-fluid d-flex flex-column justify-content-center align-items-center" style="min-height: 100vh;">
    <div class="mb-3" style="margin-top: 30px;">
      <label for="formFile" class="form-label">请上传你的数据文件</label>
      <input class="form-control" type="file" id="formFile" ref="file" @change="handleFileChange">
      
      <div class="container d-flex flex-column justify-content-center align-items-center" style="margin-top: 20px;">
        <button class="btn btn-primary" @click="uploadFile">上传</button>
      </div>
      
      <div v-if="uploadPercentage > 0" class="progress" style="margin-top: 20px;">
        <div class="progress-bar" role="progressbar" :style="{ width: uploadPercentage + '%' }" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">{{ uploadPercentage }}%</div>
      </div>
      
      <div v-if="uploadSuccess" class="alert alert-success" style="margin-top: 20px;">
        文件上传成功！
      </div>
      
      <!-- CSV Viewer Component -->
      <CsvViewer :file="selectedFile"></CsvViewer>
    </div>
  </div>
</template>

<script>
import CsvViewer from '@/components/CsvViewer.vue';
import { uploadFile } from '@/api/api';

export default {
  components: {
    CsvViewer
  },
  data() {
    return {
      uploadPercentage: 0,
      uploadSuccess: false,
      selectedFile: null, // Store selected file
    };
  },
  methods: {
    handleFileChange() {
      const files = this.$refs.file.files;
      if (files.length > 0) {
        this.selectedFile = files[0];
      }
    },
    async uploadFile() {
  this.uploadSuccess = false;
  const formData = new FormData();
  const file = this.$refs.file.files[0];
  formData.append("file", file);
  
  try {
    const response = await uploadFile(formData, progressEvent => {
      // 更新上传进度
      this.uploadPercentage = parseInt(Math.round((progressEvent.loaded / progressEvent.total) * 100));
    });
    this.uploadSuccess = true; // 设置上传成功的状态
    console.log('File uploaded successfully', response);

    // 上传成功后显示提示框
    alert("文件上传成功！");
  } catch (error) {
    this.uploadSuccess = false; // 设置上传失败的状态
    console.error('Error uploading file', error);
    
    // 可选：上传失败也显示提示框
    alert("文件上传失败，请重试。");
  }
}

  
},
};
</script>
