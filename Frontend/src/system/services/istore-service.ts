import { IPayload } from '../models';

export interface IStoreService {
    exec: <T>(cb: Promise<{}>) => Promise<IPayload<T>>
};
