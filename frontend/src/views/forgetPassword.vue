<template>
    <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
        <Header/>
        <div id="main" class="bg-primary-300 p-6 text-black">
            <div class="rounded bg-white mx-4 my-4 py-6 ">
                <div class="px-6">
                    <h1 class="text-lg font-semibold">重置密码</h1>
                </div>
            </div>
            <div class="rounded bg-white mx-4 mt-4 py-6 "> 
                <PersonalNav/>
                <div class="mt-4 mb-3 ">
                    <div class="not-prose relative">
                        <div class="ml-4 text-lg">
                        <div class="py-2 text-md">
                            <form  action="" method="post"  class="w-[300px]">
                            <div  class="flex items-center justify-between py-2">
                                <label for="old_password">注册邮箱:</label>
                                <input v-model="email" id="old_password" type="text" name="old_password" class="mx-2 outline-0 rounded border border-solid border-gray-500">
                            </div>
                            <button v-on:click.prevent="resetPassword" type="button" id="change_password" class="mb-2 rounded border bg-blue-500 text-white text-sm h-8 w-16">提交</button>
                            </form>
                        </div>
                    </div>
                    </div>
                </div>          
            </div>
        </div>
        
        <Footer/>
    </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import axios from 'axios';
import showMessage from '@/utils/message';


export default {
    name:'resetPassword',
    components:{Header,Footer},
    data:function(){
        return {
            email:'',
        }
    },
    methods:{
        resetPassword(){
            const email=this.email.trim()
            let url='/api/users/reset_password/'

            axios
                .post(url, {email:email})
                .then(response=>{
                    showMessage('发送成功','nomal',()=>{
                        this.$router.push({
                            name:'Login',
                        })
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