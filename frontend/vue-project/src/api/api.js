// api.js

import axios from 'axios';

const baseURL = 'http://localhost:8000'; // 修改为你的服务器地址

const api = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'multipart/form-data',
  },
});

const uploadFile = async (formData, onUploadProgress) => {
  try {
    const response = await api.post('/fileupload/upload/', formData, {
      onUploadProgress,
    });
    return response.data;
  } catch (error) {
    throw new Error('Error uploading file');
  }
};

export { uploadFile };
