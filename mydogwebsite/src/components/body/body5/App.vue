<template>
  <div style="position: relative;width: 1400px;height: 1000px;margin: 10px auto;">
    <ul class="md" style="position: absolute;width: 1000px;height: 900px;margin: 10px auto;list-style: none">
      <li style="text-align: center;font-size: 30px">诚邀您参加本次问卷调查</li>
      <li class="ex">
        <span>1、您的身份是</span><br>
        <RadioGroup v-model="num1" size="large">
          <Radio label="学生">学生</Radio>&nbsp;&nbsp;&nbsp;
          <Radio label="社会工作人士">社会工作人士</Radio>&nbsp;&nbsp;&nbsp;
          <Radio label="退休人员">退休人员</Radio>
        </RadioGroup>
      </li>
      <li class="ex">
        <span>2、您认为网站是否符合一个正规网站的标准？</span><br>
        <RadioGroup v-model="num2" size="large">
          <Radio label="是">是</Radio>&nbsp;&nbsp;&nbsp;
          <Radio label="否">不是</Radio>
        </RadioGroup>
      </li>
      <li class="ex">
        <span>3、对该网站您是否满意</span><br>
        <RadioGroup v-model="num3" size="large">
          <Radio label="满意">满意</Radio>&nbsp;&nbsp;&nbsp;
          <Radio label="不满意">不满意</Radio>
        </RadioGroup>
      </li>
      <li class="ex">
        <span>4、您是一位爱狗人士吗？</span><br>
        <RadioGroup v-model="num4" size="large">
          <Radio label="是">是</Radio>&nbsp;&nbsp;&nbsp;
          <Radio label="否">不是</Radio>
        </RadioGroup>
      </li>
      <li class="ex">
        <span>5、您经常会浏览哪些网站？</span><br>
        <CheckboxGroup v-model="num5" size="large">
          <checkbox size="large" label="科普类">科普类</checkbox>
          <checkbox size="large" label="新闻类">新闻类</checkbox>
          <checkbox size="large" label="购物类">购物类</checkbox>
          <checkbox size="large" label="其他">其他</checkbox>
        </CheckboxGroup>
      </li>
      <li class="ex">
        <span>6、写下一个您最喜欢的动物的名字</span><br>
        <Input size="large" v-model="num6" placeholder="你最喜欢的动物" style="width: 300px"></Input>
      </li>
      <li class="ex">
        <span>7、为本网站打分</span><br>
        <Rate v-model="num7" show-text allow-half></Rate>
      </li>
      <li class="ex">
        <span>8、写下您的建议和祝福</span><br>
        <Input v-model="num8" type="textarea" :rows=4 placeholder="enter something" style="width: 400px"></Input>
      </li>
      <li style="text-align: center;height: 100px">
        <Button @click="modal1=true" type="success" long style="width: 350px;line-height: 32px;margin-top: 60px;text-align: center">提交问卷</Button>
        <Modal
            v-model="modal1"
            title="您确认您的选择吗"
            @on-ok="ok"
            @on-cancel="cancel">
          <p>1、{{this.num1}}</p>
          <p>2、{{this.num2}}</p>
          <p>3、{{this.num3}}</p>
          <p>4、{{this.num4}}</p>
          <p>5、{{this.num5}}</p>
          <p>6、{{this.num6}}</p>
          <p>7、{{this.num7}}</p>
          <p>8、{{this.num8}}</p>
        </Modal>
      </li>
    </ul>
    <BackTop></BackTop>
  </div>
</template>

<script>
import {RadioGroup,Radio,CheckboxGroup,Checkbox,Input,Rate,BackTop} from "view-design"
  export default {
    name: "App",
    data(){
      return{
        modal1:false,
        num1:"",
        num2:"",
        num3:"",
        num4:"",
        num5:[],
        num6:"",
        num7:0,
        num8:""
      }
    },
    components:{
      Radio,
      RadioGroup,
      CheckboxGroup,
      Checkbox,
      Input,
      Rate,
      BackTop
    },
    methods:{
      ok:function (){
        // console.log(this.$refs.cb);
        if(this.num1===""||this.num2===""||this.num3===""||this.num4===""||this.num5===""
            ||this.num6===""||this.num7===""){
          alert("选择不能为空")
          return
        }
      },
      cancel:function (){
        return
      }
    }
  }
</script>

<style scoped>
  .ex {
    font-size: 20px;
    margin-left: 20px;
    margin-top: 15px;
  }
</style>