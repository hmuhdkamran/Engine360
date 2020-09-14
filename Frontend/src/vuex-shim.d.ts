import { ComponentCustomProperties } from 'vue';
import { Store } from 'vuex';
import { Router } from 'vue-router';
import { IRootStoreState } from '@/system/store/app/state';
import { ICommonState } from '.@/system/store/system/state';

import { IUser, IStatusBarData } from '@/system/models';

declare module '@vue/runtime-core' {
    interface IRootStoreState {
        reportOperation: any;
        common?: ICommonState;
    }

    interface ComponentCustomProperties {
        $store: Store<IRootStoreState>,
        $router: Router
    }
}