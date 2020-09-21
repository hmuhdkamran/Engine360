import { AuthenticationService } from '@/views/services/auth';
import { Options, Vue } from "vue-class-component";

@Options({
  name: "quick-user",
})
export default class QuickUser extends Vue {

  private userService: AuthenticationService = null;

  private displayName: string = '';
  private email: string = '';

  created(){

    this.userService = new AuthenticationService(this.$store);

  }

  mounted() {

    this.displayName = this.$store.state.common.user?.displayName;
    this.email = this.$store.state.common.user?.email;

  }

}
