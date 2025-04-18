<template>
    <Header/>
    <div class="flex items-center justify-center ">
        <div class="w-full px-2" style="max-width:1440px;">
            <div id="main" class="bg-primary-300 p-6 text-black">
                <div class="flex rounded bg-white mx-4 py-6">
                    <div class="mx-6" >
                        <div class="" style="min-height: 259px; max-height: 300px;height: 274px;">
                        <img :src="movie.image_url" class="h-full w-full">
                        </div>
                        <button v-on:click="collect_or_cancle(movie.id)" id="collect" :class="collectStatus ? 'bg-gray-500' : 'bg-blue-500'"
                        class="copy text-white w-full px-4 py-1 mt-2 text-sm bg-blue-500 rounded border">
                            {{ collectMessage }}
                        </button>
                    </div>
                    <div id="info" data-movie-id="443">
                    <ul>
                        <li class="text-lg font-semibold"> {{ movie.movie_name }}</li>
                        <li>导演: {{ movie.director }} </li>
                        <li>编剧: {{ movie.scriptwriter}}</li>
                        <li>主演: {{ movie.actors }}</li>
                        <li>语言: {{ movie.language }}</li>
                        
                        <li>首播: 2022年7月5日 </li>
                        <li>集数: 27</li>
                        
                        <li>类型: {{ movie.types }} </li>
                        <li>制片国家/地区: 
                            <span v-if="movie.region === 1">中国大陆</span>
                            <span v-else-if="movie.region === 2">中国香港</span>
                            <span v-else-if="movie.region === 3">中国台湾</span>
                            <span v-else-if="movie.region === 4">美国</span>
                            <span v-else-if="movie.region === 5">韩国</span>
                            <span v-else-if="movie.region === 6">日本</span>
                            <span v-else>其他</span>
                        </li>
                        <li>又名: {{ movie.alternate_name }} </li>
                        <li>豆瓣评分: {{ movie.rate }}</li>
                    </ul>
                    </div>
                </div>
                <div class="rounded bg-white mx-4 my-4 py-6 ">
                    <div class="px-6">
                        <h1 class="text-lg mb-6 font-semibold">简介</h1>
                        <p>
                            {{ movie.review }}
                        </p>
                    </div>
                </div>
                <div id="download_info" class="rounded bg-white mx-4 mt-4 py-6 "> 
                    <h1 class="text-lg mb-6 font-semibold px-6">网盘地址</h1>
                    <div v-if="movie.download_info" class="px-6">
                        <div v-if="downloadInfo">
                            {{ movie.download_info }}
                        </div>
                        <div v-else class="flex justify-center items-center mx-6 rounded h-28 bg-gray-500">
                            <button v-on:click="check_member_stats" id="check_member" class="rounded text-center bg-blue-500">查看网盘地址</button>
                        </div>
                    </div>
                    <div  v-else class="px-6">
                        <li>
                            暂无网盘信息
                        </li>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <Footer/>
</template>


<script>

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import axios from 'axios'
import showMessage from '@/utils/message'

export default{
    name : "MovieDetail",
    components:{Header,Footer},

    data:function(){
        return{
            movie:{ },
            collectStatus:false,
            collectMessage:'',
            downloadInfo:false,
            userInfo:'',
        }
    },

    mounted(){
        this.get_movie_info()

        //判断用户是否登录
        if (!this.$store.state.isLogin)
        {
            this.collectStatus=false
            this.collectMessage='添加收藏'
        }
        else 
        {
            const movie_id=this.$route.params.id
            this.get_collect_status(movie_id)
        }
    },

    methods: {
        get_movie_info: function () {
            axios
                .get('/api/movies/'+this.$route.params.id)
                .then(response => (this.movie=response.data))

        },

        get_collect_status:function(movie_id)
        {
            let url='/api/collects/'+movie_id+'/is_collected/'
            const token=localStorage.getItem('token')
            axios
                .get(url,{
                    headers:{
                        'Authorization':'JWT '+ token
                    }
                })
                .then(response =>{
                    this.collectStatus=response.data.is_collected
                    if (this.collectStatus) {
                        this.collectMessage='取消收藏'
                    }
                    else {
                        this.collectMessage='添加收藏'
                    }
                })
                
        },

        collect_or_cancle:function(movie_id){
            if (!this.$store.state.isLogin)
            {
                showMessage('请先登录','error',()=>{
                    this.$router.push({
                    name:'Login'})
                })
            }
            else {
                this.collectStatus ? this.cancle_collect_movie(movie_id) : this.collect_movie(movie_id)
            }
        },

        collect_movie:function(movie_id) {
            let url='/api/collects/'
            const token=localStorage.getItem('token')
            axios
                .post(url , {movie_id:movie_id} , {
                    headers:{
                        'Authorization':'JWT ' + token
                    }
                })
                .then(response=>{
                    this.collectStatus=true
                    this.collectMessage='取消收藏'
                    showMessage(this.collectMessage,'nomal')
                })
                .catch(error => {
                    showMessage('收藏失败')
                })
        },

        cancle_collect_movie:function(movie_id) {
            let url='/api/collects/' + movie_id + '/'
            const token=localStorage.getItem('token')
            axios
                .delete(url , {
                    headers:{
                        'Authorization':'JWT ' + token
                    }
                })
                .then(response=>{
                    this.collectStatus=false
                    this.collectMessage='添加收藏'
                    showMessage(this.collectMessage,'nomal')
                })
                .catch(error => {
                    showMessage('取消收藏失败')
                })
        },

        // 判断用户状态
        check_member_stats()
        {
            if (!this.$store.state.isLogin)
            {
                showMessage('请先登录')
                return
            }
            const accessToken = window.localStorage.getItem('token'); 
            axios
                .get('/api/users/me',{
                    headers: {
                        'Authorization': `JWT ${accessToken}` 
                    }
                })
                
                .then(response=>{
                    this.userInfo = response.data
                    if (this.userInfo.profile.is_upgrade){
                        this.downloadInfo=true
                    } else
                    {
                        alert('请购买会员卡')
                        this.$router.push({
                            name:'memberCard'
                        })
                    }
                })
        }
    }
}


</script>