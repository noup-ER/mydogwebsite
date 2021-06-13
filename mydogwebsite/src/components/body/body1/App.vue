<template>
  <div style="position: relative;width: 1400px;height: 880px;margin: 10px auto">
    <!--    轮播图-->
    <Carousel autoplay loop class="loopp" :autoplay-speed="3000">
      <CarouselItem>
        <img src="../../../static/image/dogphotos/fivehfiveh/dog1.jpg" style="height: 500px;width: 500px">
      </CarouselItem>
      <CarouselItem>
        <img src="../../../static/image/dogphotos/fivehfiveh/dog2.jpg" style="height: 500px;width: 500px">
      </CarouselItem>
      <CarouselItem>
        <img src="../../../static/image/dogphotos/fivehfiveh/dog3.jpeg" style="height: 500px;width: 500px">
      </CarouselItem>
      <CarouselItem>
        <img src="../../../static/image/dogphotos/fivehfiveh/dog4.jpg" style="height: 500px;width: 500px">
      </CarouselItem>
    </Carousel>
    <!--    弹性布局12按钮-->
    <ul class="ul1">
      <li><button class="bt">狗狗导航</button></li>
      <li><button class="bt">狗狗工具</button></li>
      <li><button class="bt">狗狗装束</button></li>
      <li><button class="bt">狗狗品种</button></li>
      <li><button class="bt">狗狗美图</button></li>
      <li><button class="bt">狗狗攻略</button></li>
      <li><button class="bt">狗狗壁纸</button></li>
      <li><button class="bt">狗狗性格</button></li>
      <li><button class="bt">狗狗命相</button></li>
      <li><button class="bt">狗狗毛发</button></li>
      <li><button class="bt">狗狗健康</button></li>
      <li><button class="bt">狗狗天赋</button></li>
    </ul>
    <!--    第二栏-->
    <div style="position: absolute;border: 2px rgba(221,221,221,1) solid;width: 470px;height: 850px;left: 520px;top:10px;">
      <div style="position: absolute;top:0px;bottom:0px;left:0px;right:0px;margin: 1px auto;border-bottom: 1px rgba(221,221,221,1) solid; width: 380px;height: 50px">
          <h2 style="position: absolute;bottom: -1px;border-bottom: 3px solid rgba(242,71,61,1);width: 92px;text-align: center;color: rgba(242,71,61,1);border-collapse: collapse">狗狗专栏</h2>
          <div class="md" style="top:15px;left: 329px;width: 50px;height: 30px;text-align: center;cursor: pointer">
            <Icon type="md-more"></Icon>
            <span style="line-height: 30px">更多</span>
          </div>
      </div>
      <ul class="md ul2" style="top:70px;margin: 1px auto;width: 400px;height: 400px;text-align: center">
        <li><p><a>狗狗们这回有救了！人大代表建议立法反虐待动物...</a></p></li>
        <li><p><a>农业农村部首次明确33种家养畜禽种类，狗和蛙类不在其中</a></p></li>
        <li><p><a>请支持！全国人大代表高子程：虐待动物影响中国国际形象...</a></p></li>
        <li><p><a>看到主人被恶狗攻击,拉布拉多英勇而上,不顾生命救下了主人!</a></p></li>
        <li><p><a>国任保险推出3个月免费宠物医疗保险，从此养宠无忧...</a></p></li>
        <li><p><a>进口宠物食品消费者洞察报告发布</a></p></li>
        <li><p><a>中华田园犬或将被禁养，某大V博主声称...</a></p></li>
        <li><p><a>农业农村部：狗拟不列入畜禽遗传资...</a></p></li>
        <li><p><a>喜大普奔，深圳全面禁食猫狗肉！</a></p></li>
      </ul>
      <Divider style="position: absolute;top:460px"></Divider>
      <table class="md" style="top:483px;margin: 1px auto;width: 400px;height: 300px">
        <tr>
          <td style="width: 50px"><a>情感</a></td>
          <td style="width: 20px">|</td>
          <td><a>会拜拜的流浪毛孩子，曾经也是有家的</a></td>
        </tr>
        <tr>
          <td style="width: 50px"><a>守护</a></td>
          <td style="width: 20px">|</td>
          <td><a>2个月的泰迪怎么喂?两个月的小泰迪怎么养</a></td>
        </tr>
        <tr>
          <td style="width: 50px"><a>美容</a></td>
          <td style="width: 20px">|</td>
          <td><a>怎么给哈士奇化妆？</a></td>
        </tr>
        <tr>
          <td style="width: 50px"><a>趣事</a></td>
          <td style="width: 20px">|</td>
          <td><a>一只狗能陪伴老人多旧？</a></td>
        </tr>
        <tr>
          <td style="width: 50px"><a>民俗</a></td>
          <td style="width: 20px">|</td>
          <td><a>不吃狗肉是不是约定俗成？</a></td>
        </tr>
        <tr>
          <td style="width: 50px"><a>趣事</a></td>
          <td style="width: 20px">|</td>
          <td><a>邻居家才买回来两个月大的拉布拉多不胫而走！</a></td>
        </tr>
        <tr>
          <td style="width: 50px"><a>奇妙</a></td>
          <td style="width: 20px">|</td>
          <td><a>狗的脚掌中有一种奇妙的物质</a></td>
        </tr>
      </table>
    </div>
    <!--    第三栏-->
    <div style="position: absolute;width: 388px;height: 850px;right: 10px;top:10px;border: 1px solid rgba(221,221,221,1)">
      <Tabs style="">
        <TabPane label="最新资讯" name="name1" class="tp">
          <ul class="md"  style="position: relative;width: 285px;height: 700px;margin: 10px auto">
            <li v-for="(i,index) in items(flag)" :key="index" style="margin-top:10px;font-size: 11px "><a>{{i}}</a></li>
            <li style="margin-top: 20px"><div style="cursor: pointer" @click="refresh"><Icon type="ios-refresh" size="large"></Icon><span>刷新</span></div></li>
          </ul>
        </TabPane>
        <TabPane label="趣味周边" name="name2" class="tp">趣味周边</TabPane>
        <TabPane label="宠物医疗" name="name3" class="tp">宠物医疗</TabPane>
        <TabPane label="狗狗视频" name="name4" class="tp">狗狗视频</TabPane>
      </Tabs>
    </div>
    <!--    返回顶部-->
    <back-top></back-top>
  </div>
</template>

<script>
import {Carousel,CarouselItem,BackTop,Icon,Divider,Tabs,TabPane} from "view-design"
import axios from "axios";
  export default {
    name: "App",
    data(){
      return {
        ans:["1"],
        flag:true
      }
    },
    computed:{
      items(){
        return function (flag){
          if(flag){
            this.flag = false;
            axios.get("http://127.0.0.1:8000/gwtn/").then(
                res=>{
                  this.ans = res.data
                  return res.data}).catch(err=>{return err})
          }
          return this.ans
        }
      }
    },
    components:{
      Carousel,
      CarouselItem,
      BackTop,
      Icon,
      Divider,
      Tabs,
      TabPane
    },
    methods:{
      refresh:function (){
        this.flag = true
      }
    }
  }
</script>

<style scoped>
  .loopp {
    position: absolute;
    top:10px;
    left: 10px;
    width:500px;
    height: 500px;
  }

  ul {
    list-style: none;
  }

  .ul1 {
    position: absolute;
    width: 500px;
    height: 300px;
    /*border: 1px black solid;*/
    left: 10px;
    top: 520px;
    display: flex;
    list-style: none;
    flex-wrap: wrap;
    background: url("../../../static/image/body1/bg1.jpg");
  }

  .ul1 li {
    margin-top: 20px;
    margin-left: 18px;
    float: left;
  }

  .ul2 li {
    margin-top: 20px;
    margin-left: 18px;
    float: left;
  }

  .bt {
    flex: 1;
    width: 100px;
    height: 40px;
    background-color: rgba(178,235,215,1) ;
  }

  .bt:hover {
    background-color: rgba(245, 130, 32, .9);
    color: white;
    box-shadow: 0px 0px 1px 1px rgba(0,0,0,.4);
    cursor: pointer;
  }

  a {
    color: black;
    font-size: 14px;
  }

  a:hover {
    color: red;
  }


</style>