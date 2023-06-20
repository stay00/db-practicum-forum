<template>
    <el-row class="flex-row-reverse justify-between expand">
        <el-col :sm="18">
            <!-- <el-empty v-if='empty' description="No User" /> -->
            <Article></Article>
        </el-col>
        <el-col :sm="6">
            <Topics></Topics>
        </el-col>
    </el-row>
</template>
<script setup>
import Topics from './Topics.vue'
import Articles from './Articles.vue'
const empty = true
import axios from '@/api'


const AllArticles = async () => {
    let res = await axios.get('/api/article/')
    console.log("all-articles", res)
}

AllArticles()
</script>

<style scoped>
.expand {
    flex-grow: 1;
    display: flex;
}
</style>
