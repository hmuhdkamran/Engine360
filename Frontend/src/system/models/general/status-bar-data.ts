import { IPayloadMessage } from '..';

export interface IStatusBarData extends IPayloadMessage {
    uri?: string;
    timeout?: number;
};