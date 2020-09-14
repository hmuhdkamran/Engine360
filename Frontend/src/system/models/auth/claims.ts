import { IUser } from '..';

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
