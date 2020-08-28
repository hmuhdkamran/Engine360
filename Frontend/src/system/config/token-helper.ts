import { GlobalConfig } from '.';
import { ILoginProvider, IUser, DefaultUser, IJwtToken } from '../models';

import { default as jwtDecode } from "jwt-decode";
import { default as base64 } from "base-64";

import { mapKeys, pick } from './helper';

export class TokenHelper {
    public static getAccessToken(): string {
        return localStorage.getItem(GlobalConfig.auth.accessTokenKey);
    }

    public static setAccessToken(token: string): void {
        return localStorage.setItem(GlobalConfig.auth.accessTokenKey, token);
    }

    public static removeAccessToken(): void {
        return localStorage.removeItem(GlobalConfig.auth.accessTokenKey);
    }

    public static getProvider(): ILoginProvider {
        let value = localStorage.getItem(GlobalConfig.auth.externalProviderKey);
        return value ? JSON.parse(base64.decode(value)) : null;
    }

    public static setProvider(provider: ILoginProvider): void {
        localStorage.setItem(
            GlobalConfig.auth.externalProviderKey,
            base64.encode(JSON.stringify(provider))
        );
    }

    public static removeProvider(): void {
        localStorage.removeItem(GlobalConfig.auth.externalProviderKey);
    }

    public static parseUserToken(token: string): IUser {
        let user: IUser = Object.assign({}, DefaultUser);

        if (token) {
            let decodedToken: IJwtToken = jwtDecode(token);
            const ns = GlobalConfig.claimsNamespace;

            if (!user.authenticated) user.authenticated = true;
            let name =
                decodedToken[
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name"
                ];
            let email =
                decodedToken[
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
                ] || null;
            let sid =
                decodedToken[
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/sid"
                ];
            let roles =
                decodedToken[
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/role"
                ];

            let claimNames = Object.keys(decodedToken).filter(key => key.startsWith(ns));
            let claims = <any>(
                mapKeys(pick(decodedToken, claimNames as any), (value: any, key: any) =>
                    key.replace(ns, "").substring(1)
                )
            );

            user.claims = claims;
            user.cultureName = claims.culturename;
            user.displayName = name ? name[1] : null;
            user.name = user.email = email;
            user.roles = Array.isArray(roles) ? roles : [roles];
            user.verified = true; // claims.verified === "true" ? true : false;
            user.exp = new Date(decodedToken.exp * 1000);
            user.userId = sid;
            user.timeZoneId = claims.timezoneid;
        }

        return user;
    }

    public static getBearerToken() {
        let token = localStorage.getItem(GlobalConfig.auth.accessTokenKey);

        return {
            Authorization: token
                ? "Bearer " + localStorage.getItem(GlobalConfig.auth.accessTokenKey)
                : null
        };
    }

    public static isTokenCurrent(value: string | IUser) {
        let user: IUser = null;

        if (typeof value === "string") {
            user = TokenHelper.parseUserToken(value);
        } else {
            user = value;
        }

        if (!user) return null;
        else return user.exp && user.exp > new Date();
    }
}
