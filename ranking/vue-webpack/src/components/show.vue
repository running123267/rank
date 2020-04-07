<template>
    <div>
        <table border="1">
            <tr>
                <td>排名</td>
                <td>客户号</td>
                <td>分数</td>
            </tr>

            <tr v-for="i in userlist">

                <td>{{i.rank}}</td>
                <td>{{i.name}}</td>
                <td>{{i.grade}}</td>

            </tr>

            <tr>
                <td>{{alist.rank}}</td>
                <td>{{alist.name}}</td>
                <td>{{alist.grade}}</td>
            </tr>
        </table>
    </div>
</template>

<script>
    export default {
        name: "show",
        data:function () {
            return{
                userlist:[],
                alist:[]
            }
        },
        mounted() {
            this.axios({
                url:'/api/show/',
                data:{},
                method:'get'
            }).then(res=>{

                if (res.data.code==200){
                    this.userlist = res.data.messet_age
                    this.alist = res.data.alist

                }
            })
        }
    }
</script>

<style scoped>

</style>