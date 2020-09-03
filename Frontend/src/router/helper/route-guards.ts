import { NavigationGuard, RouteLocationNormalized, RouteLocation, NavigationGuardNext } from 'vue-router';

import { IUser } from '@/system/models';
import { TokenHelper } from '@/system/config';
import { IClaimsHelper, IRouteMeta, IRouteGuardOptions } from '../models';
import { ClaimHelper } from '.';
import Vue from "vue";

function routeCheck(user: IUser, helper: IClaimsHelper, meta: IRouteMeta): boolean {
    let hasClaims = meta.claims;
    let matchAny = !meta.any ? true : meta.any;

    if ((hasClaims || meta.private) && !user.authenticated) return true;

    if (hasClaims) {
        if (Array.isArray(meta.claims)) {
            if (matchAny) {
                return !helper.satisfiesAny(user, meta.claims);
            } else {
                return !helper.satisfies(user, meta.claims);
            }
        } else {
            return true;
        }
    } else {
        return false;
    }
}

function verifyCheck(user: IUser, meta: IRouteMeta): boolean {
    if (user.authenticated && (meta.private || meta.claims))
        return !user.verified;
    else return false;
}

export function RouteGuards(options: IRouteGuardOptions): NavigationGuard {
    let fn = async (to: RouteLocationNormalized, from: RouteLocationNormalized, next: NavigationGuardNext) => {

        let claimsHelper: ClaimHelper;
        let sendTo: RouteLocation = {
            fullPath: '',
            hash: '',
            matched: null,
            meta: null,
            name: '',
            params: null,
            path: '',
            query: null,
            redirectedFrom: null
        };

        let user = options.resolveUser() || TokenHelper.parseUserToken(TokenHelper.getAccessToken());

        if (to.matched.some(r => routeCheck(user, claimsHelper, r.meta))) {

            if (user.authenticated && to.meta.claims) {
                next(options.forbiddenRouteName);
            } else {
                next(options.loginRouteName);
            }
        } else if (
            to.name !== options.verifyRouteName &&
            to.matched.some(r => verifyCheck(user, r.meta))
        ) {
            next(options.loginRouteName);
            window.scrollTo(0, 0);
        } else {
            next();
            window.scrollTo(0, 0);
        }
    };
    return fn;
}