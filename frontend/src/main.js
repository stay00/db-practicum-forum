import { createApp } from 'vue'
// import './style.css'
import App from './App.vue'
import router from '@/router'
import 'virtual:windi.css'
import store from '@/store'

import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';

// highlightjs
import hljs from 'highlight.js';

VMdEditor.use(githubTheme, {
  Hljs: hljs,
});

const app = createApp(App)
app.use(store)
app.use(router)
app.use(VMdEditor)
app.mount('#app')

