import { ActionTree, ActionContext } from 'vuex';
import { IRootStoreState } from './state';
import { RootStoreTypes } from '@/system/models/store/types';

export const Actions: ActionTree<IRootStoreState,{}> = {

    reportOperation: (Injectee: ActionContext<IRootStoreState, any>, value: any) =>{

        Injectee.commit(RootStoreTypes.reportOperation, value);

    }
    
}