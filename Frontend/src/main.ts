import { createApp } from "vue";
import ApplicationView from "./views/app.vue";
import "./registerServiceWorker";

import { PageView } from "@/components";

import router from './router';
import Store from './system/store/app';

var app = createApp(ApplicationView)
  .use(Store)
  .use(router);

app.component("page-view", PageView);

app.mount("#app");
