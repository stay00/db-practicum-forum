<template>
    <el-menu :default-active="activeIndex" router class="text-dark font-bold" mode="horizontal" background-color="#ffffff"
        active-text-color="#5b21b6" @select="handleSelect">
        <el-menu-item :disabled="true">
            <span class="text-2xl text-dark">Tongji</span>
        </el-menu-item>
        <div class="flex-grow"></div>
        <el-menu-item v-if="isAdmin" index="/forum/dashboard">
            管理
        </el-menu-item>
        <el-menu-item index="1">
            探索
        </el-menu-item>
        <el-menu-item index="/forum/index">
            主页
        </el-menu-item>
        <el-menu-item index="2">
            专区
        </el-menu-item>
        <el-menu-item :disabled="true">
            <Search />
        </el-menu-item>
        <el-menu-item>
            <User />
        </el-menu-item>
        <div class="items-center">
        </div>
    </el-menu>
    <el-backtop :right="100" :bottom="100" />
</template>

<script setup>
// import Canvas from '@/components/canvas.vue'
import Search from '@/components/search.vue'
import User from '@/components/usericon.vue'
import { ref, reactive, computed } from 'vue'
import { useStore } from 'vuex'
const store = useStore()
const isAdmin = computed(() => {
    return store.state.user['level'] != 1
})
const defaultItem = isAdmin ? '/admin/dashboard' : '/forum'
let activeIndex = ref(defaultItem)

const handleSelect = (select) => {
    activeIndex = select
    console.log(activeIndex)
}

</script>
<style scoped>
.flex-grow {
    flex-grow: 1;
}

.text-dark {
    color: #0D0C22
}
</style>