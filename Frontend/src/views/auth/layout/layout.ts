import { Options, Vue } from "vue-class-component";

@Options({
  name: "AuthLayoutView",
})
export default class AuthLayoutView extends Vue {
  mounted(){
    document.body.className = "hold-transition login-page";
  }
}
