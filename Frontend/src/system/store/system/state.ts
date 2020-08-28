import { IUser, IStatusBarData } from '@/system/models';

export interface ICommonState {
    isLoading: boolean;
    user: IUser;
    statusBar: IStatusBarData;
};