# 大纲

开发技术栈

项目架构绘制

![在这里插入图片描述](https://img-blog.csdnimg.cn/769ee23deb86490b8194213ead7d13cb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5bGF5LmL6Iul,size_20,color_FFFFFF,t_70,g_se,x_16)

项目目录

组件树

环境变量

## bug 汇总

### vue 部分

1. vite 报错：[vite] Internal server error: At least one <template> or <script> is required in a single file component.

   解决方案：template 内不为空

2. 



## 数据库部分

1. 数据库定义
2. 数据库关系
3. ORM
4. 联合主键

## 视图部分

1. vue3 和 vite 介绍

2. 项目目录结构

3. 创建

   ```bash
   npm init vite
   cd 
   npm run dev
   # 安装路由
   npm install vue-router --save
   # 安装插件
   npm install element-plus --save
   npm i unplugin-vue-components unplugin-auto-import -D
   npm install vite-plugin-windicss windicss -D
   npm install axios --save
   npm install vuex@next --save
   npm i js-cookie --save 
   
   ```

   创建 router 文件夹，在其中创建 index.js

4. vite 配置

   配置 @ 别名和 element-plus 按需导入，查一下原理

   ```js
   import { defineConfig } from 'vite'
   import vue from '@vitejs/plugin-vue'
   import AutoImport from 'unplugin-auto-import/vite'
   import Components from 'unplugin-vue-components/vite'
   import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
   import { resolve } from 'path'
   
   // https://vitejs.dev/config/
   export default defineConfig({
     plugins: [
       vue(),
       AutoImport( {
         resolvers: [ElementPlusResolver()],
       }),
       Components({
         resolvers: [ElementPlusResolver()],
       }),
     ],
     resolve: {
       alias: {
         '@': resolve(__dirname, 'src'),
       },
     },
   })
   
   ```

    **这里还可以补充 server，环境变量文件夹以及后端 api 代理的配置** 

   - 使用学号的后四位作为端口号 3246

5. vue 生命周期

   

   ![组件生命周期图示](https://cn.vuejs.org/assets/lifecycle.16e4c08e.png)

   - 组合式 API 中，setup 事实上就是替代了选项式 API 中的 create
   - mount：子组件被挂载，自身 DOM 树也已经被挂载
   - update：响应式状态更新

6. element-plus

   按需引入

   响应式布局

   表单

   - 验证涉及到的属性 :rule, ref, :model, prop
   - 密码验证时有个 **bug**，有关blur...

7. WendiCSS

8. ajax

   axios

   - 向 api 发送请求
   - 请求拦截器
   - 异步 Promise，async，await 不懂

9. flask

   跨域请求 flask_cors

   [Flask 开启跨域 - JunCode - 博客园 (cnblogs.com)](https://www.cnblogs.com/Jaryer/p/14713828.html)

   vite开启跨域不太懂

   

   web api

   [一文搞懂什么是RESTful API - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/334809573)

   登录操作，token

   [js-cookie/js-cookie: A simple, lightweight JavaScript API for handling browser cookies (github.com)](https://github.com/js-cookie/js-cookie)

   | URL         | 请求方法 | 作用     |
   | ----------- | -------- | -------- |
   | /api/login/ | POST     | 登陆验证 |

   

10. 普通用户和管理员有不同的视图，vuex 状态

11. 环境变量配置

12. 模糊查询

13. 注册

    前端自定义校验

14. 响应式

    主页在手机尺寸时，边栏需要收缩到一个按钮