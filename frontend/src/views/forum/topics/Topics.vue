<template>
    <el-container class="full flex flex-col">
        <!-- <h5 class="mb-2">Default colors</h5> -->
        <el-menu class="full" default-active="1" mode="vertical" @open="handleOpen" @close="handleClose">
            <el-menu-item index="1">
                <el-icon>
                    <Top />
                </el-icon>
                <span>热门</span>
            </el-menu-item>
            <el-sub-menu index="2">
                <template #title>
                    <el-icon>
                        <Reading />
                    </el-icon>
                    <span>学习区</span>
                </template>
                <el-menu-item index="1-1">课程</el-menu-item>
                <el-menu-item index="1-2">考试</el-menu-item>
            </el-sub-menu>
            <el-menu-item index="3">
                <el-icon>
                    <Coffee />
                </el-icon>
                <span>生活区</span>
            </el-menu-item>
        </el-menu>
    </el-container>
</template>
  
<script lang="ts" setup>
import {
    Top,
    Menu as IconMenu,
    Coffee,
    Reading,
} from '@element-plus/icons-vue'
const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
</script>

<style scoped>
.full {
    height: 100%;
    width: 100%;
}
</style>
  