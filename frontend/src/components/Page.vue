<template>
    <div class="min-h-screen min-w-screen bg-gray-100 flex flex-col">
        <div class="no-expand">
            <Navigator></Navigator>
        </div>
        <div class="expand">
            <router-view></router-view>
        </div>
    </div>
</template>

<script setup>
import Navigator from '@/components/navigator.vue'
</script>

<style scoped>
.no-expand {
    flex-grow: 0;
}

.expand {
    flex-grow: 1;
    display: flex;
}
</style>