<template>
  <div>
    <h1>222</h1>
    <button @click="fetchData">Fetch Data</button>
    <div v-if="data">{{ data }}</div>
    <div v-if="error">{{ error }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      data: null,
      error: null
    };
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://localhost:8000/polls');
        this.data = response.data;
        this.error = null;
      } catch (error) {
        this.data = null;
        this.error = 'Error fetching data';
        console.error('Error fetching data', error);
      }
    }
  }
};
</script>
