import { StoreService } from '@/system/services';
import { Store } from 'vuex';
import { TokenHelper, GlobalConfig } from '@/system/config';
import { ICredential, IAccessToken, IUser, IPayload, PayloadMessageTypes, DefaultUser } from '@/system/models';
import Axios, { AxiosResponse } from 'axios';

export class AuthenticationService extends StoreService {

  constructor(store: Store<{}>) {
    super(store);
  }

  login(credentials: ICredential) {
    let onSuccess = (token: IAccessToken) => {
      if (token) {
        TokenHelper.setAccessToken(token.access_token);

        return TokenHelper.parseUserToken(token.access_token);
      }
    };

    return this.exec<IAccessToken>(Axios.post(GlobalConfig.uri.auth + 'login', credentials))
      .then(value => this.processPayload(value))
      .then(onSuccess);
  }

  logout() {
    let onSuccess = (res: AxiosResponse) => {
      let payload: IPayload<IAccessToken> = res.data;

      if (payload.message.messageTypeId === PayloadMessageTypes.success) {
        let user: IUser = Object.assign({}, DefaultUser);

        TokenHelper.removeAccessToken();
        window.localStorage.removeItem('microsoft-auth');

        return user;
      } else {
        throw new Error(payload.message.text);
      }
    };

    return Axios.put(GlobalConfig.uri.auth + 'logout', null)
      .then(onSuccess)
      .then(() => location.reload());
  }
}