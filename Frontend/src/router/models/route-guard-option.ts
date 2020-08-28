import { IUser } from '@/system/models';

export interface IRouteGuardOptions {
    resolveUser(): IUser;
    forbiddenRouteName: string;
    loginRouteName: string;
    verifyRouteName: string;
    store: any;
  };