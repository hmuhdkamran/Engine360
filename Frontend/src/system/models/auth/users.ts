
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