<template>
  <div class="titlebar" style="position: relative;width: 1400px;height: 20px;margin: auto">
    <Dropdown style="position: absolute;right:10px">
      <a href="#">
        用户
        <Icon type="ios-arrow-down"></Icon>
      </a>
      <DropdownMenu slot="list">
        <DropdownItem>注册</DropdownItem>
        <DropdownItem>设置</DropdownItem>
        <DropdownItem><div @click="goout">登出</div></DropdownItem>
        <DropdownItem>个性主题</DropdownItem>
      </DropdownMenu>
    </Dropdown>
  </div>
</template>

<script>
import {Dropdown,DropdownMenu,DropdownItem,Icon} from "view-design"
  export default {
    name: "App",
    components:{
      Dropdown,
      DropdownMenu,
      DropdownItem,
      Icon
    },
    methods:{
      goout:function (){
        this.$router.push("/login")
      }
    }
  }
</script>

<style scoped>

</style>