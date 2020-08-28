import { IClaimsHelper } from '../models/claims-helper';
import { IUser } from '@/system/models';

export class ClaimHelper implements IClaimsHelper {

    satisfies(user: IUser, claims: string[]): boolean {
        var satisfied: boolean = false;
        if (!user.roles)
            return satisfied;

        user.roles.forEach(assigned => {
            claims.forEach(checking => {
                if (assigned === checking) {
                    satisfied = true;
                }
            });
        });

        return satisfied; 
    }

    satisfiesAny(user: IUser, claims: string[]): boolean {
        var satisfied: boolean = false;
        if (!user.claims)
            return satisfied;

        user.roles.forEach(assigned => {
            claims.forEach(checking => {
                if (assigned === checking) {
                    satisfied = true;
                }
            });
        });

        return satisfied;
    }
}