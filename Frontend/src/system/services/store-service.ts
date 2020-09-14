import { Store } from 'vuex';
import { IPayload, IStatusBarData, PayloadMessageTypes, StoreTypes } from '../models';

import { PayloadMapper } from '../config';
import { IStoreService } from '.';

interface IProcessPayloadOptions<T> {
    timeout?: number,
    uri?: string,
    messageTypeIds?: string[]
}

export abstract class StoreService implements IStoreService {

    constructor(protected store: Store<{}>) { }

    handleFulfilled<T>(data: T) {

        return this.store.dispatch(StoreTypes.loadingState, false)
            .then(() => new PayloadMapper().fromObject<T>(data));
    }

    handleRejection<T>(reason: any) {

        return this.store.dispatch(StoreTypes.loadingState, false)
            .then(() => this.store.dispatch(StoreTypes.updateStatusBar, reason))
            .then(() => new PayloadMapper().fromObject<T>(reason));
    }

    processPayload<T>(payload: IPayload<T>, options?: IProcessPayloadOptions<T>): Promise<T> {

        let message = payload.message;
        options = options || {};
        let messageTypeIds = options.messageTypeIds || [PayloadMessageTypes.error, PayloadMessageTypes.failure];

        let messageTypeId = messageTypeIds.find(o => o === message.messageTypeId);

        if (messageTypeId) {

            options.timeout = options.timeout || 1500;

            let statusBarData: IStatusBarData = {
                messageTypeId: message.messageTypeId,
                text: message.text,
                timeout: options.timeout,
                title: message.title,
                uri: options.uri
            };

            return this.store.dispatch(StoreTypes.updateStatusBar, statusBarData)
                .then(() => Promise.reject(null));

        } else {
            return Promise.resolve(payload.data);
        }
    }

    exec<T>(cb: Promise<{}>): Promise<IPayload<T>> {

        let onFulfilled = (value: any) => this.handleFulfilled<T>(value);
        let onRejection = (reason: any) => this.handleRejection<T>(reason);

        return this.store.dispatch(StoreTypes.loadingState, true)
            .then(() => cb)
            .then(onFulfilled, onRejection);
    }
}