<template>
  <div class="searchbar">
    <img src="../../static/image/searchlogo.png" class="doglogo">
    <div style="position: absolute;top:99px;left:45px;font-size: 17px;font-weight: 500">dogwebsite.cn</div>
    <Input search enter-button="Search" placeholder="请输入内容" size="large" style="position: absolute;right: 41px;top:12px;width:457px;"/>
    <ul style="list-style: none;position: absolute;width: 400px;right: 110px;top:76px;font-size: 15px">
      <li>热搜:</li>
      <li><a href="#">哈士奇</a></li>
      <li><a href="#">边牧</a></li>
      <li><a href="#">狗会咬人吗</a></li>
      <li><a href="#">狗粮怎么选择</a></li>
    </ul>
      <div class="timeset" style="position: absolute;margin-left: 300px;width: 355px;height: 80px;margin-top: 17px">
        <times></times>
      </div>
  </div>
</template>

<script>
import {Input} from "view-design"
import times from "./timeset"
  export default {
    name: "App",
    components:{
      Input,
      times
    }
  }
</script>

<style scoped>
  .searchbar {
    position: relative;
    width: 1315px;
    height: 130px;
    /*border: black solid 1px;*/
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
  }

  .doglogo {
    display: block;
    position: absolute;
    height: 120px;
    top:-10px;
    left: 20px;
  }

  li {
    float: left;
    margin-left: 10px;
  }

  a {
    color: black;
  }

  a:hover {
    color: red;
  }

</style>