import { ActionTree, ActionContext } from 'vuex';
import { ICommonState } from './state';
import { TokenHelper } from '@/system/config';
import { IStatusBarData, IPayloadMessage, StoreTypes, IUser, PayloadMessageTypes } from '@/system/models';

function isStatusBarData(object: any): object is IStatusBarData {
    return object === undefined ? null : 'uri' in object || 'timeout' in object;
}

function isPayloadMessage(object: any): object is IPayloadMessage {
    return object === undefined ? null : 'messageTypeId' in object;
}

export const Actions: ActionTree<ICommonState, any> = {

    loading: (injectee: ActionContext<ICommonState, any>, loading: boolean) => {

        injectee.commit(StoreTypes.loadingState, loading);
    },

    updateLocale: (injectee: ActionContext<ICommonState, any>, cultureName: string) => {

        injectee.commit(StoreTypes.updateLocale, cultureName);
    },

    updateUser: (injectee: ActionContext<ICommonState, any>, userData: string | IUser) => {

        let payload: IUser = null;

        if (typeof userData === 'string')
            payload = TokenHelper.parseUserToken(userData);
        else
            payload = userData

        injectee.commit(StoreTypes.updateUser, payload);
    },

    updateStatusBar: (injectee: ActionContext<ICommonState, any>, data: Error | IStatusBarData | IPayloadMessage) => {

        let payload: IStatusBarData = null;

        if (data === null) {
            payload = {
                messageTypeId: null,
                text: null,
                timeout: null,
                title: null,
                uri: null
            };
        }
        else if (data instanceof Error) {

            payload = {
                messageTypeId: PayloadMessageTypes.error,
                text: data.message,
                timeout: null,
                title: data.name,
                uri: null
            };

        } else if (isStatusBarData(data)) {

            payload = data;

        } else if (isPayloadMessage(data)) {

            payload = {
                messageTypeId: data.messageTypeId,
                text: data.text,
                timeout: null,
                title: data.title,
                uri: null
            };

        }

        if (payload)
            injectee.commit(StoreTypes.updateStatusBar, payload);
    },

    updateTimeZone: (injectee: ActionContext<ICommonState, any>, timeZoneId: string) => {

        injectee.commit(StoreTypes.updateTimeZone, timeZoneId);
        
    }
};