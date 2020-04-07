<template>
    <div>

        上传客户号：<input v-model="name">
        上传分数：<input v-model="grade">
        <button v-on:click="affirm">确认</button>
        <router-link :to="{'name':'show'}">查看排名表</router-link>
    </div>
</template>

<script>
    export default {
        name: "uploading",
        data:function () {
            return{
                name:'',
                grade:''
            }
        },
        methods:{
            affirm:function () {
                this.axios({
                url:'/api/index/',
                data:{'name':this.name,'grade':this.grade},
                method:'post'
            }).then(res=>{

                if (res.data.code==200){
                    alert('添加成功')
                }else{
                     alert(res.data.message)
                }
            })
            }

        }
    }
</script>

<style scoped>

</style>