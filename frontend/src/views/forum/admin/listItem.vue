<template>
    <el-descriptions class="" :column="3" :size="size" border>
        <el-descriptions-item>
            <template #label>
                <div class="cell-item">
                    <el-icon :style="iconStyle">
                        <user />
                    </el-icon>
                    Username
                </div>
            </template>
            kooriookami
        </el-descriptions-item>
        <el-descriptions-item>
            <template #label>
                <div class="cell-item">
                    <el-icon :style="iconStyle">
                        <Message />
                    </el-icon>
                    Email
                </div>
            </template>
            18100000000
        </el-descriptions-item>
        <el-descriptions-item>
            <template #label>
                <div class="cell-item">
                    <el-icon :style="iconStyle">
                        <tickets />
                    </el-icon>
                    Level
                </div>
            </template>
            <el-tag size="small">社区管理员</el-tag>
            <!-- <el-button type="primary" opacity="1"> -->
                <el-icon :style="iconStyle"
                @click="detail">
                    <InfoFilled />
                </el-icon>
            <!-- </el-button> -->
        </el-descriptions-item>
    </el-descriptions>
</template>

<script setup>
import {
    Message,
    Tickets,
    User,
    InfoFilled
} from '@element-plus/icons-vue'

const detail = () => {
    console.alert('test')
}
</script>

<style scoped>
.el-descriptions {
    margin-top: 20px;
}

.cell-item {
    display: flex;
    align-items: center;
}

.margin-top {
    margin-top: 20px;
}
</style>