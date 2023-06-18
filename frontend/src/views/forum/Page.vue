<template>
    <div class="min-h-screen min-w-screen bg-gray-100">
        <Navigator></Navigator>
        <router-view></router-view>
        <slot></slot>
    </div>
</template>

<script setup>
import Navigator from '@/components/navigator.vue'
</script>