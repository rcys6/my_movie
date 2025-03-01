const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

// 配置前端转发
module.exports = {
  devServer : {
      // 代理
      proxy: {
            'api':{
              target:'http://127.0.0.1:8000/api',

              changeOrigin: true,//允许跨域 可以代理反向的地址
              pathRewrite:{ //重写路径
                '^/api':'' 
              }
            }
      }
  }
};