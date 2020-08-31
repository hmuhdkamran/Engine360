export interface IUser {
    authenticated: boolean;
    claims: {};
    cultureName?: string;
    createdOn?: Date;
    displayName?: string ;
    email?: string ;
    enabled?: boolean;
    name?: string ;
    roles: string[];
    username: string ;
    verified?: boolean;
    exp?: Date;
    userId?: number;
    timeZoneId?: string;
};

export interface ICredential {
    username: string;
    password: string;
};

export interface IAccessToken {
    access_token: string;
    expires_on: number;
};

export const DefaultUser = <IUser>{
    authenticated: false,
    claims: {},
    cultureName: "en",
    displayName: null,
    email: null,
    name: null,
    username: null,
    roles: [],
    timeZoneId: "Pakistan Standard Time",
    verified: false
};

export const SecurityRoleClaims = {
    Admin: "admin",
    Client: "client",
    SiteAdmin: "siteadmin",
    User: "user"
};

export const SecurityClaims = {
    Api: "api",
    SiteSettings: "sitesettings",
    UserSettings: "usersettings"
};
