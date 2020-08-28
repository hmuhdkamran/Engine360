import { createStore } from "vuex";
import { Mutations } from './mutations';
import { Actions } from './actions';
import { CommonModule } from '../system';
import { IRootStoreState } from './state';

const Store = createStore<IRootStoreState>({
    state: {
        reportOperation: null
    },
    mutations: Mutations,
    actions: Actions,
    modules: {
        common: CommonModule
    }
});

if ((<any>module).hot) {
    (<any>module).hot.accept([
        './actions',
        './mutations'
    ], () => {
        Store.hotUpdate({
            actions: require('./actions').default,
            mutations: require('./mutations').default
        })
    })
};

export default Store;