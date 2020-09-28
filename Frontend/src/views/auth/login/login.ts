import { Options, Vue } from "vue-class-component";

import { AuthenticationService } from '../../services/auth';
import { ICredential, StoreTypes, PayloadMessageTypes } from '@/system/models';

@Options({ name: "LoginView" })
export default class LoginView extends Vue {

  private auth: AuthenticationService = null;
  private user: ICredential = { username: '', password: '' };

  created() {

    this.auth = new AuthenticationService(this.$store);

  }

  mounted() {
    this.user.username = 'admin@c3.com';
    this.user.password = 'P@ssw0rd';
  }

  login(): void {

    var credentials: ICredential = {
      username: (this.user.username.toLowerCase()),
      password: this.user.password
    }

    this.auth.login(credentials)
      .then((value) => this.$store.dispatch(StoreTypes.updateUser, value))
      .then(() => this.$store.dispatch(StoreTypes.updateStatusBar, null))
      .then(() => this.$router.push("/home"))
      .then(() => location.reload())
      .catch(() => this.$store.dispatch(StoreTypes.updateStatusBar, {
        text: 'Invalid UserName or Password',
        title: 'Error',
        messageTypeId: PayloadMessageTypes.error
      }));
  }
}
