<template>
    <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
        <Header/>
        <div class="text-center text-2xl p-8">
            激活你的账号
        </div>
        <div class="flex items-center justify-center">
            <div class="w-1/4 p-4 bg-gray-100 rounded-lg shadow-lg">
                <div class="text-black text-center p-4">
                    请点击下方按钮，激活账号
                </div>
                <div class="flex justify-center">
                    <button v-on:click="activate" class="bg-green-500 text-white px-4 py-2 rounded">激活账号</button> 
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>


<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import showMessage from '@/utils/message';

import axios from 'axios';

export default {
    name: 'ActivateEmail',
    components : { Header,Footer },
    methods:{
        activate()
        {
            const uid=this.$route.params.uid
            const token=this.$route.params.token
            const formData={
                uid:uid,
                token:token,
            }
            const url = '/api/users/activation/'
            axios
                .post(url,formData)
                .then( response =>{
                    showMessage('注册成功，请到邮箱激活账号','nomal',()=>{
                        this.$route.push({name:'Login'})
                    })
                })
                .catch(error=>{
                const errorData=error.response.data
                const errrormessage=Object.values(errorData).flat();
                for (let i=0;i<errrormessage.length;i++)
                {
                    showMessage(errrormessage[i])
                }
                })
        }
    }
}

</script>