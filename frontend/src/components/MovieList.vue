<template>
    <div class="flex items-center justify-center">
        <div class="w-full px-2" style="max-width:1440px;">
            <div id="movie-list" class="p-2 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
                <!-- key 来提供排序提升 -->
                <div class="movie" v-for="movie in info.results" :key="movie.id">
                    <a href=""> 
                        <div class="relative">
                            <div v-if="movie.image_url" class="cover">
                                <img :src="movie.image_url"  alt="" class="rounded h-full w-full">
                            </div>
                            <div v-else>
                                <img src="" alt="" class="rounded h-full w-full">
                            </div>
                            <div v-if="movie.is_top" class="rounded absolute top-0 bg-purple-600 px-1 text-sm">
                                置顶
                            </div>
                            <div v-if="movie.quality === 1" class="rounded absolute bottom-0 right-0 bg-blue-500 px-1 text-sm ">
                                720p
                            </div>
                            <div v-else-if="movie.quality === 2" class="rounded absolute bottom-0 right-0 bg-blue-500 px-1 text-sm ">
                                1080p
                            </div>
                            <div v-else-if="movie.quality === 3" class="rounded absolute bottom-0 right-0 bg-blue-500 px-1 text-sm ">
                                4k
                            </div>
                        </div>
                        <p> {{ movie.movie_name }}({{movie.release_year}})</p>
                        <p class="text-sm text-primary-200">{{movie.language}}</p>
                    </a>
                </div>

            </div>  
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'MovieList',
    data: function() {  //定义数据
        return {
            info:''
        }
    },

    mounted() { // axios发送请求
        this.get_movie_data()
    },

    methods:{
        get_movie_data:function(){
            let url="/api/movies"
            const page=Number(this.$route.query.page)
            if (!isNaN(page)|| page!==0)
            {
                url=url+'/?page='+page
            }


            axios
                .get(url)

                // 处理结果
                .then( response => (this.info = response.data ))
                // 处理错误
                .catch (error=>{
                    console.log(error)
                })
        }
    }

}
    
</script>