<template>
  <div>
    <div class="all">
      <inputbox></inputbox>
    </div>
  </div>
</template>

<script>
  export default {
    name: "App",
    components:{
      inputbox:()=>import("./inputbox")
    },
    methods:{
    }
  }
</script>

<style scoped>
  .all {
    position: absolute;
    width: 100%;
    height: 100%;
    background: url("../../static/image/loginbg.jpg");
    background-size: cover;
  }
</style>