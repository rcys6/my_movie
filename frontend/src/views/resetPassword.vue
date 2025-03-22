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
                <div class="mt-4 mb-3 ">
                    <div class="not-prose relative">
                        <div class="ml-4 text-lg">
                        <div class="py-2 text-md">
                            <form  action="" method="post"  class="w-[300px]">
                            <div class="flex items-center justify-between py-2">
                                <label for="new_password">新密码:</label>
                                <input v-model="new_password" id="new_password" type="password" name="new_password" class="mx-2 outline-0 rounded border border-solid border-gray-500">
                            </div>
                            <div class="flex items-center justify-between py-2">
                                <label for="confirm">确认密码:</label>
                                <input v-model="re_password" id="confirm_password" type="password" name="confirm_password"  class="mx-2 outline-0 rounded border border-solid border-gray-500">
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
    import Header from '@/components/Header.vue'
    import Footer from '@/components/Footer.vue'

    import axios from 'axios'
    import showMessage from '@/utils/message.js'

    export default{
        name:'restPassword',
        components:{Footer,Header},
        data:function(){
            return {
                uid:'',
                token:'',
                new_password:'',
                re_password:'',
            }
        },
        methods:{
            resetPassword(){
                const uid=this.$route.params.uid
                const token=this.$route.params.token
                const new_password=this.new_password.trim()
                const re_password=this.re_password.trim()

                if(new_password === '')
                {
                    showMessage('新密码不能为空')
                    return
                }
                if(re_password === '')
                {
                    showMessage('确认密码不能为空')
                    return
                }

                if(new_password !== re_password)
                {
                    showMessage('两次密码不一致')
                    return
                }


                let url='/api/users/reset_password_confirm/'
                const dataForm={
                    uid:uid,
                    token:token,
                    new_password:new_password,
                    re_new_password:re_password,
                }
                axios
                    .post(url,dataForm)
                    .then(response=>{
                        showMessage('重置成功','nomal',()=>{
                            this.$router.push({
                                name:'Login'
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