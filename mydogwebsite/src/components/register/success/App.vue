<template>
  <div>
    <span>恭喜你注册成功</span>
    <br>
    <button @click="jump">点击跳转回登陆界面</button>
  </div>
</template>

<script>
export default {
  name: "App",
  methods:{
    jump:function (){
      this.$router.push("/login")
    }
  }
}
</script>

<style scoped>

</style>