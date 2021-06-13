import Vue from 'vue'
import VueRouter from 'vue-router'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

Vue.use(VueRouter)

const routes = [
  {
    path:"/",
    redirect:"/login"
  },
  {
    path: "/login",
    component:()=>import("login/App")
  },
  {
    path:"/register",
    component:()=>import("register/App")
  },
  {
    path:"/body",
    component:()=>import("body/body0/App"),
    redirect: "/body/body1",
    children:[
      {
        path:"/body1",
        component:()=>import("body/body1/App")
      },
      {
        path:"/body2",
        component:()=>import("body/body2/App")
      },
      {
        path:"/body3",
        component:()=>import("body/body3/App")
      },
      {
        path:"/body4",
        component:()=>import("body/body4/App")
      },
      {
        path:"/body5",
        component:()=>import("body/body5/App")
      },
    ]
  },
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
