import Vue from 'vue'
import App from './App'
import router from './router'
//导包
import axios from 'axios'

Vue.config.productionTip = false;

//配置
Vue.prototype.axios =axios;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
