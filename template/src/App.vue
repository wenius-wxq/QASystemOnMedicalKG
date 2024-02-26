<template>
  <div id="app">

    <el-select v-model="value" :loading="loading" @click="updateOptions()">
	    <el-option v-for="item in options" :key="item.id" :label="item.file" :value="item.id"></el-option>
    </el-select>


  </div>
</template>

<script>
export default {
  data() {
      return {
        options: [],
        list: [],//传回后端的参数
      };
  },
  methods:{
    //点击后更新下拉选项
    updateOptions(){
      this.list=[{value:''}, {value:''}];//按需修改
      axios.post('http://127.0.0.1:8000/api/getnewoption/', this.list).then(res=>{
        console.log(res);
        this.options=res.data;
      }).catch((mes)=>{
        this.$message.warning("请求失败")
      });},
  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
