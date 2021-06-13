<template>
  <div class="rebg">
    <div class="inputbox">
      <ul>
        <li style="margin-top: 10px"><span style="font-size: 30px">欢迎成为狗狗网的一员</span></li>
        <li style="margin-top: 20px">
          <span type="text" style="font-size: 20px;line-height: 40px">账号名称: </span>
          <Input placeholder="请输入账号名称" size="large" style="width: 300px" v-model="reaccount">
            <Icon type="ios-contact" slot="prefix" />
          </Input>
        </li>
        <li style="margin-top: 20px">
          <span style="font-size: 20px;line-height: 40px">账号密码: </span>
          <Input type="password" placeholder="请输入账号密码" size="large" style="width: 300px" v-model="repw1">
            <Icon type="ios-lock-outline" slot="prefix" />
          </Input>
        </li>
        <li style="margin-top: 20px">
          <span style="font-size: 20px;line-height: 40px">确认密码: </span>
          <Input type="password" placeholder="请输入确认密码" size="large" style="width: 300px" v-model="repw2">
            <Icon type="ios-lock-outline" slot="prefix" />
          </Input>
        </li>
        <li style="margin-top: 20px">
          <span type="text" style="font-size: 20px;line-height: 40px">电子邮箱: </span>
          <Input placeholder="请输入电子邮箱" size="large" style="width: 300px" v-model="reemail">
            <Icon type="ios-mail" slot="prefix" />
          </Input>
        </li>
        <li style="margin-top: 20px">
          <span type="text" style="font-size: 20px;line-height: 40px"> QQ 号码: </span>
          <Input placeholder="请输入qq号码" size="large" style="width: 300px" v-model="reqq">
            <Icon type="logo-tux" slot="prefix" />
          </Input>
        </li>
        <li style="margin-top: 20px">
          <span type="text" style="font-size: 20px;line-height: 40px"> 手机号码: </span>
          <Input placeholder="请输入手机号码" size="large" style="width: 300px" v-model="remo">
            <Icon type="ios-call" slot="prefix" />
          </Input>
        </li>
        <li style="margin-top: 40px">
          <Button type="success" long @click="reregister">Register</Button>
        </li>
      </ul>
      <button class="back" @click="gologin">
        <Icon type="ios-home" />
      </button>
    </div>
  </div>
</template>

<script>
import {Input,Icon,Button} from "view-design"
import axios from "axios";
  export default {
    name: "App",
    components:{
      Input,
      Icon,
      Button
    },
    data(){
      return{
        reaccount:"",
        repw1:"",
        repw2:"",
        reemail:"",
        reqq:"",
        remo:""
      }
    },
    methods:{
      gologin:function (){
        this.$router.push("/login")
      },
      reregister:function (){
        //获得重复用户名
        axios({
          method:"get",
          url:"http://127.0.0.1:8000/getuserdate/",
          type:"json",
          timeout:5000
        }).then(res =>{
          console.log(/[1]/.test("1"))
          // 判断输入内容
          if (this.reaccount===""
              ||this.repw1===""
              ||this.repw2===""||this.reemail===""||this.reqq===""||this.remo===""){
            alert("输入内容不得为空");
            return
          }
          // 判断用户是否存在
          if(this.reaccount in res.data){
            alert("用户名已存在，请重新设置用户名")
            return;
          }
          //判断两次密码输入
          if(this.repw1 != this.repw2){
            alert("两个密码输入不一致，请重新输入")
            return;
          }
          //判断手机号
          if(/^[1-9]\d{10}$/.test(this.remo)===false){
            alert("手机号码设置错误，请重新输入")
            return
          }
          //数据库登记并实施跳转
          axios({
            method:"GET",
            url:"http://127.0.0.1:8000/adduserdata/",
            type:"json",
            timeout:5000,
            params:{
              "account":this.reaccount,
              "pw":this.repw1,
              "email":this.reemail,
              "qq":this.reqq,
              "mobile":this.remo
            }
          }).then(()=>{
            this.$router.push("/registersu")
          }).catch(err=>{
            alert(err)
          })
        }).catch(err=>{
          alert("连接服务器失败，错误"+err)
          return
        })

      }
    }
  }
</script>

<style scoped>
  .rebg {
    position: absolute;
    width: 100%;
    height: 100%;
    background: url("../../static/image/registerbg.jpg");
    background-size: cover;
  }

  .inputbox {
    width: 500px;
    height: 550px;
    background-color: rgba(178,224,223,.9);
    position: relative;
    margin: 60px auto;
    border-radius: 20px;
    text-align: center;
  }

  ul{
    position: absolute;
    width: 400px;
    height: 400px;
    left: 50px;
    list-style: none;
  }

  .back {
    width: 40px;
    height: 40px;
    background-color: pink;
    z-index: 2;
    position: absolute;
    left: 12px;
    top:12px
  }
</style>