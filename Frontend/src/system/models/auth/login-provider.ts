import { RouteLocationNormalized } from 'vue-router';

export interface ILoginProvider {
    access_token?: string;
    nonce: string;
    providerId: string;
    responseUri: string;
    returnUri: string;
    uri: string;
};

export const LoginProviders = {
    Local: 'LOCAL AUTHORITY',
    Google: 'GOOGLE',
    Microsoft: 'MICROSOFT'
};

export interface ILoginClient {
    clientId: string;
    iconClass: string;
    localeKeys: { name: string };
    providerId: string;
    getAccessToken(route: RouteLocationNormalized): string;
    getUri(provider: ILoginProvider): string;
};