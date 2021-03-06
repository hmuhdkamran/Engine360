import { RouteRecordRaw } from "vue-router";
import { AuthLayoutView, LoginView, HomeView, LayoutView } from './route-modules';

export const RouteConfig: Array<RouteRecordRaw> = [
    {
        component: LayoutView, path: '/', meta: { private: true, transition: 'slide-left' },
        children: [
            { component: HomeView, name: 'Home', path: 'home' },
        ]
    },
    {
        component: AuthLayoutView, path: '/', meta: { transition: 'slide-right' },
        children: [
            { component: LoginView, name: 'Login', path: 'login' },
        ]
    },
];