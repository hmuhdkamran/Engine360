import { RouteLocationNormalized } from 'vue-router';
import { ILoginProvider } from '..';

export interface ILoginClient {
    clientId: string;
    iconClass: string;
    localeKeys: { name: string };
    providerId: string;
    getAccessToken(route: RouteLocationNormalized): string;
    getUri(provider: ILoginProvider): string;
};
