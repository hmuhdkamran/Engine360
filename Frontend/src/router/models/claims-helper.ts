import { IUser } from '@/system/models';

export interface IClaimsHelper {
    satisfies(user: IUser, claims: string[]): boolean;
    satisfiesAny(user: IUser, claims: string[]): boolean;
}