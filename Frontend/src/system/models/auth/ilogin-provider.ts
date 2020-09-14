
export interface ILoginProvider {
    access_token?: string;
    nonce: string;
    providerId: string;
    responseUri: string;
    returnUri: string;
    uri: string;
};