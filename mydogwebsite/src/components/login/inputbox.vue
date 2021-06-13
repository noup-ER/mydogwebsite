<template>
  <div class="box">
    <ul class="input1" style="list-style: none">
      <li style="height: 50px"><span class="char">dog website welcome</span></li>
      <li style="margin-top: 50px;">
        <Input type="text" placeholder="Username" style="width: 300px;margin:auto;" v-model="account">
        <Icon type="ios-person-outline" slot="prepend"></Icon>
        </Input>
      </li>
      <li style="margin-top: 20px">
        <Input type="password" placeholder="Password" style="width: 300px;margin:auto;" v-model="pw">
          <Icon type="ios-lock-outline" slot="prepend"></Icon>
        </Input>
      </li>
    </ul>
    <div style="position:absolute;top: 195px;right: 53px"><a @click="goregi">立即注册</a></div>
    <Checkbox style="position:absolute;top: 231px;right: 213px" v-model="single" @click="changeflag">我已阅读服务条款</Checkbox>
    <Button type="primary" :disabled="!single" @click="gobody" style="position:absolute;top: 281px;right: 54px;width:299px ">登录</Button>
  </div>
</template>

<script>
import {Input,Icon,Checkbox,Button} from "view-design"
import axios from "axios"

export default {
  name: "inputbox",
  components:{
    Input,
    Icon,
    Checkbox,
    Button
  },
  data(){
    return {
      single:false,
      account:null,
      pw:null,
      data:null
    }
  },
  methods:{
    // 条款与登录
    changeflag:function (){
      if (this.single){
        this.single=false;
      }else{
        this.single=true;
      }
    },
    // 跳转去注册
    goregi:function (){
      this.$router.push("/register")
    },
    // 跳转去首页
    gobody:function (){
      axios({
        method:"get",
        url:"http://127.0.0.1:8000/getuserdate/",
        type:"json",
        timeout:5000
      }).then(res =>{
        this.data = res.data
        if (!(this.account in this.data && this.pw === this.data[this.account])){
          alert("登录失败,请检查账号或密码是否填写正确")
          return
        }
        this.$router.push("/body")
      }).catch(err=>{
        alert("连接服务器失败，错误"+err)
        return
      })
    }
  }
}
</script>

<style scoped>
  .box {
    position: relative;
    right: -984px;
    top: 145px;
    background: url("../../static/image/logininputboxbg.jpg");
    background-size: cover;
    width: 407px;
    height: 450px;
    border-radius: 20px;
    text-align: center;
  }

  .char {
    font-size: 30px;
    font-weight: 700;
    line-height: 50px;
  }
</style>