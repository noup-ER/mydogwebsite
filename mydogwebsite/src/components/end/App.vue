<template>
  <div class="endbox">
    <div style="position: absolute;width: 100%;height: 300px;top: 0px;text-align: center">
        <img src="../../static/image/end/wechat.png" style="height: 200px;position: absolute;margin: 10px auto" class="md">
      <div style="position: absolute;top:220px;color: white;font-size: 15px" class="md">欢迎贵客添加好友了解更多关于狗奇闻秘事</div>
    </div>
    <ul class="md" style="width: 100%;height: auto;color: white;top:280px;text-align: center">
      <li>地址:浙江省乐清市</li>
      <li>想投稿关于狗狗的新鲜事可加qq:759270724</li>
      <li>狗狗是人类的好朋友，让我们共建和谐美丽家园</li>
      <li>Copyright ©2021 localhost 狗狗网 版权所有</li>
      <li>备案信息：京ICP备17171717号-2 · 京ICP备17171717号-3</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "App"
}
</script>

<style scoped>
  .endbox {
    position: relative;
    width: 100%;
    height: 450px;
    bottom: 0px;
    background:url("../../static/image/end/endbg.jpg");
    background-size: cover;
  }

  .md li {
    margin-top: 10px;
  }
</style>