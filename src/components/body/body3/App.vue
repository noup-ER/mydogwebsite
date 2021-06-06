<template>
  <div style="position: relative;width: 1400px;height: 300px;margin: 10px auto;">
    <div class="bt"><Button type="primary" @click="open(false)">这个页面发生了什么</Button></div>
  </div>
</template>

<script>
import {Button} from "view-design"
export default {
  name: "App",
  components:{
    Button
  },
  methods: {
    open (nodesc) {
      this.$Notice.open({
        title: ' (✿◠‿◠)',
        desc: nodesc ? '' : '这个页面尚未修复完成，请耐心等待T T'
      });
    }
  }
}
</script>

<style scoped>
  .bt  {
    position: absolute;
    width: 200px;
    height: 100px;
    top:0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    margin:10px auto;
  }
</style>