import { StoreService } from '@/system/services';
import { Store } from 'vuex';
import { TokenHelper, GlobalConfig } from '@/system/config';
import { ICredential, IAccessToken, IUser } from '@/system/models';
import Axios from 'axios';

export class AuthenticationService extends StoreService {

    constructor(store: Store<{}>) {
        super(store);
      }

      login(credentials: ICredential) {
        debugger;
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
}