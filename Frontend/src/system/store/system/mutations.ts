import { MutationTree } from 'vuex';
import { ICommonState } from './state';
import { IUser, DefaultUser, IStatusBarData } from '@/system/models';

export const Mutations: MutationTree<ICommonState> = {

    loading: (state: ICommonState, loading: boolean) => {
        state.isLoading = loading;
    },

    updateLocale: (state: ICommonState, cultureName: string) => {
        let user = Object.assign({}, state.user);
        user.cultureName = cultureName;
        state.user = user;
    },

    updateUser: (state: ICommonState, user: IUser) => {
        state.user = Object.assign({}, user || DefaultUser);
    },

    updateStatusBar: (state: ICommonState, data: IStatusBarData) => {
        state.statusBar = Object.assign({}, data);
    },

    updateTimeZone: (state: ICommonState, timeZoneId: string) => {
        let user = Object.assign({}, state.user);
        user.timeZoneId = timeZoneId;
        state.user = user;
    },
};