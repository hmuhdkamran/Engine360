import { ComponentCustomProperties } from 'vue';
import { Store } from 'vuex';
import { Router } from 'vue-router';

import { IUser, IStatusBarData } from '@/system/models';

declare module '@vue/runtime-core' {
    interface State {
        isLoading: boolean;
        user: IUser;
        statusBar: IStatusBarData;
    }

    interface ComponentCustomProperties {
        $store: Store<State>,
        $router: Router
    }
}