import { MutationTree } from 'vuex';
import { IRootStoreState } from './state';

export const Mutations: MutationTree<IRootStoreState> = {

    reportOperation(state: IRootStoreState, value) {

        state.reportOperation = value;
        
    }

};