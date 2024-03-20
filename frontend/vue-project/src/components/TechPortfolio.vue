<template>
  <section id="program" class="portfolio">
    <div class="container" data-aos="fade-up">
      <div class="section-title">
        <h2>技术实现</h2>
        <p>详细的技术实现</p>
      </div>
      <div class="row" data-aos="fade-up" data-aos-delay="100">
        <div class="col-lg-12 d-flex justify-content-center">
          <ul id="portfolio-flters">
            <li data-filter="*" class="filter-active">全部</li>
            <li data-filter=".filter-app">前端设计</li>
            <li data-filter=".filter-card">后端设计</li>
            <li data-filter=".filter-web">算法及模型</li>
          </ul>
        </div>
      </div>
      <div class="row portfolio-container" data-aos="fade-up" data-aos-delay="200">
        <div class="col-lg-4 col-md-6 portfolio-item" v-for="(item, index) in portfolioItems" :key="index" :class="item.filter">
          <div class="portfolio-wrap">
            <img :src="item.imgSrc" class="img-fluid" :alt="item.title">
            <div class="portfolio-info">
              <h4>{{ item.title }}</h4>
              <p>{{ item.subtitle }}</p>
              <div class="portfolio-links">
                <a :href="item.imgSrc" data-gallery="portfolioGallery" class="portfolio-lightbox" :title="item.title"><i class="bx bx-plus"></i></a>
                <a :href="item.detailLink" target="_blank" title="More Details"><i class="bx bx-link"></i></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import AOS from 'aos';
import 'aos/dist/aos.css'; //需要引入 CSS
import { onMounted } from 'vue';
onMounted(() => {
  AOS.init();
});
export default {
  data() {
    return {
      portfolioItems: [
        // 示例项目
        {
          title: "前端",
          subtitle: "服务界面",
          imgSrc: "../static/assets/img/portfolio/portfolio-1.jpg",
          detailLink: "/program/",
          filter: "filter-app"
        },
        // 更多项目...
      ]
    };
  }
};
</script>

<style scoped>
/* 样式 */
</style>
