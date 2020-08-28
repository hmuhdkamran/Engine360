import { ICommonState } from '../system/state';

export interface IRootState {
    reportOperation: any;
}

export interface IRootStoreState extends IRootState {
    common?: ICommonState
}