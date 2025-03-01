<template>
  <Header/>
  <div class="about">
    <h1 class="bg-gray-500 text-3xl font-bold">This is an about page</h1>
  </div>
  <Footer/>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'


export default {
    name:'About',
    components: {
        Header,Footer
    }
}

</script>