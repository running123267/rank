import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import uploading from '@/components/uploading'
import show from '@/components/show'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },{
      path: '/uploading',
      name: 'uploading',
      component: uploading
    },{
      path: '/show',
      name: 'show',
      component: show
    },
  ]
})
