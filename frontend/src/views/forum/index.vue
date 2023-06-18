<template>
    <el-container>
        <el-main>
            <el-empty v-if='empty' description="No User" />

        </el-main>
        <el-aside width="200px">Aside</el-aside>
    </el-container>
</template>
<script setup>
import Nav from "@/components/navigator.vue";
const empty = true
</script>
