<template>
  <div id="app">
    <el-table
        :data="currentPriceData"
        style="width: 100%"
        stripe>
      <el-table-column
          prop="标题"
          label="标题"
          fixed="left">
      </el-table-column>
      <el-table-column
          prop="区域"
          label="区域">
      </el-table-column>
      <el-table-column
          prop="小区"
          label="小区">
      </el-table-column>
      <el-table-column
          prop="面积"
          label="面积">
      </el-table-column>
      <el-table-column
          prop="单价"
          label="单价">
      </el-table-column>
      <el-table-column
          prop="总价"
          label="总价">
      </el-table-column>
      <el-table-column
          prop="户型"
          label="户型">
      </el-table-column>
      <el-table-column
          prop="类型"
          label="住宅类型">
      </el-table-column>
      <el-table-column
          prop="楼层"
          label="所属楼层">
      </el-table-column>
      <el-table-column
          prop="总层"
          label="总层数">
      </el-table-column>
    </el-table>
    <el-pagination
        layout="prev,pager,next"
        background
        :total="priceDataLines"
        :page-size="this.pageSize"
        :current-page.sync="currentPage"
        @current-change="handleCurrentChange">
    </el-pagination>
  </div>
</template>

<script>
import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI)

export default {
  name: 'App',
  data() {
    return {
      //全部的房价信息
      allPriceData: [],
      //每页显示条数
      pageSize: 10,
      //当前显示的页码
      currentPage: 1
    }
  },
  computed: {
    //经过筛选的房价行数
    priceDataLines() {
      return this.filteredPriceData.length;
    },
    //筛选后的房价信息
    filteredPriceData() {
      return this.filterPriceData();
    },
    //当前页的房价信息
    currentPriceData() {
      return this.filteredPriceData.slice((this.currentPage - 1) * 10,
          (this.currentPage - 1) * 10 + this.pageSize + 1);
    }
  },
  methods: {
    handleCurrentChange() {
    },
    //筛选需要显示的内容
    filterPriceData() {
      return this.allPriceData;
    }
  },
  mounted() {
    //读取数据
    this.allPriceData = require('../../python_spider/test.json');
  }
}
</script>

<style>
#app {

}
</style>
