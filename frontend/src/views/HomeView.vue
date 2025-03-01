<template>
  <header>
    <meta name="referrer" content="no-referrer">
  </header>
  
  <Header/>
  <MovieList/>
  <Footer/>
</template>

<script>
// @ is an alias to /src

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'HomeView',
  components: {
    Header,Footer,MovieList
  }
}
</script>
