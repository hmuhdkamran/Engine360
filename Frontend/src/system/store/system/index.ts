import { Module } from 'vuex';
import { ICommonState } from './state';
import { DefaultUser } from '@/system/models';
import { Mutations } from './mutations';
import { Actions } from './actions';

export const CommonModule: Module<ICommonState, {}> = {
    state: {
        isLoading: false,
        user: Object.assign({}, DefaultUser),
        statusBar: {
            messageTypeId: null,
            text: null,
            title: null,
            uri: null,
            timeout: null
        }
    },
    mutations: Mutations,
    actions: Actions
};
