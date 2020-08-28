import { IPayloadMessage } from '..';


export interface IPayload<T> {

    data: T;

    message: IPayloadMessage;
}