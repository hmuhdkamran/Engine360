
import { useRouter } from 'vue-router';
import Axios, { AxiosRequestConfig, AxiosError, AxiosResponse } from 'axios';
import { TokenHelper } from '.';

let initialized: boolean = false;

function handle(status: number, exclude: number[]) {
    if (exclude.length === 0) return true;
    else return exclude.find(o => o === status) === undefined;
}

export function UseAxios() {
    let router = useRouter();

    if (!initialized) {
        Axios.interceptors.request.use((config: AxiosRequestConfig) => {
            if (!config.headers["Authorization"]) {
                let bearerToken = TokenHelper.getBearerToken();

                if (bearerToken.Authorization)
                    Object.assign(config.headers, bearerToken);
            }

            if (!config.maxRedirects || config.maxRedirects === 5)
                config.maxRedirects = 0;

            return config;
        });

        Axios.interceptors.response.use(undefined, (config: AxiosError) => {
            let response: AxiosResponse = config.response;
            let exclude: any = [];

            if (response.status === 401 && handle(response.status, exclude)) {
                let location: string =
                    response.headers["location"] || response.headers["Location"];

                if (location) {
                    let redirectTo = "/" + location;
                    window.setTimeout(() => router.replace(redirectTo), 200);
                }
            }

            if (response.status === 403 && handle(response.status, exclude)) {
                window.setTimeout(() => router.replace("/forbidden"), 200);
            }

            return config;
        });

        initialized = true;
    }
}
