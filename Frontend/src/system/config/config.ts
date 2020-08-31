
interface IUriConfig {
    auth?: string;
    content?: string;
    site?: string;
    services?: string;
};

const uri: IUriConfig = {};

const addProp = (obj: {}, propName: string, value: string) => {
    Object.defineProperty(obj, propName, {
        enumerable: false,
        get: () => {
            return 'http://127.0.0.1:5000' + value;
        }
    });
};

addProp(uri, 'auth', '/api/auth/');
addProp(uri, 'content', '/api/content/');
addProp(uri, 'site', '');
addProp(uri, 'services', '/api/');

const config = {
    uri: uri,
    claimsNamespace: 'https://eng360/claims',
    auth: {
        accessTokenKey: 'AUTH-LOCAL',
        externalProviderKey: 'AUTH-EXTERNAL'
    },
    uopt: 'UOPT',
    xsrf: {
        cookieName: 'XSRF-TOKEN',
        headerName: 'X-XSRF-TOKEN'
    }
};

export default config;
