import { createRouter, createWebHistory } from "vue-router";
import { RouteConfig, RouteNames, RouteGuards } from './helper';
import Store from '@/system/store/app';

let options = {
  resolveUser: () => Store.state.common.user,
  forbiddenRouteName: RouteNames.forbidden,
  loginRouteName: RouteNames.login,
  verifyRouteName: RouteNames.verify,
  store: Store
};

const router = createRouter({
  history: createWebHistory(),
  linkActiveClass: 'active',
  routes: RouteConfig,
});

router.beforeEach(RouteGuards(options));

export default router;