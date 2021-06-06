<template>
  <div id="app">
    <!--    登录-->
    <div v-show="checkroute('login',1)">
      <login></login>
    </div>
    <!--    注册-->
    <div v-show="checkroute('register',1)">
      <register></register>
    </div>
    <!--    主页-->
    <div v-show="checkroute('body',1)">
      <body0></body0>
      <div v-show="checkroute('body1',2)">
        <body1></body1>
      </div>
      <div v-show="checkroute('body2',2)">
        <body2></body2>
      </div>
      <div v-show="checkroute('body3',2)">
        <body3></body3>
      </div>
      <div v-show="checkroute('body4',2)">
        <body4></body4>
      </div>
      <div v-show="checkroute('body5',2)">
        <body5></body5>
      </div>
      <end></end>
    </div>
    <!--    注册成功-->
    <div v-show="checkroute('registersu',1)">
      <registersu></registersu>
    </div>
  </div>
</template>

<script>
  export default {
    name:"App",
    components:{
      login:()=>import("login/App"),
      register:()=>import("register/App"),
      body0:()=>import("body/body0/App"),
      body1:()=>import("body/body1/App"),
      body2:()=>import("body/body2/App"),
      body3:()=>import("body/body3/App"),
      body4:()=>import("body/body4/App"),
      body5:()=>import("body/body5/App"),
      registersu:()=>import("register/success/App"),
      end:()=>import("end/App")
    },
    computed:{
      checkroute(){
        return function(a,num){
          let pathname = this.$route.path;
          let ls = pathname.split("/")
          if (num>=ls.length){
            return false
          }
          return ls[num] === a
        }
      },
    }
  }
</script>

<style>
  * {
    margin:0px;
    padding:0px;
  }

  .md {
    position: absolute;
    top:0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
  }
</style>
