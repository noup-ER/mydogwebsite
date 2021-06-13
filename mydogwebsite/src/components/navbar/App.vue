<template>
  <div style="width: 100%;height: 60px;background-color: #f05b72;position: relative;">
    <div style="position:absolute;display: flex;height: 100%;width: 80%;left: 0px;right: 0px;top:0px;bottom: 0px;margin: auto">
        <div class="navcho" @click="c1"><span>首页</span></div>
        <div class="navcho" @click="c2"><span>狗狗百科</span></div>
        <div class="navcho" @click="c3"><span>爱狗须知</span></div>
        <div class="navcho" @click="c4"><span>狗狗美照</span></div>
        <div class="navcho" @click="c5"><span>填写问卷</span></div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "APP",
    methods:{
      c1:function (){
        this.$router.push("/body/body1")
      },
      c2:function (){
        this.$router.push("/body/body2")
      },
      c3:function (){
        this.$router.push("/body/body3")
      },
      c4:function (){
        this.$router.push("/body/body4")
      },
      c5:function (){
        this.$router.push("/body/body5")
      }
    }
  }
</script>

<style scoped>
  .navcho {
    height: 100%;
    width: 80px;
    flex: 1;
    text-align: center;
    cursor: pointer;
  }

  .navcho:hover {
    background-color: #d93a49;
  }

  span {
    line-height: 60px;
    color: white;
    font-size: 20px;
  }
</style>