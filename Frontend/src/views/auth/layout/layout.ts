import { Options, Vue } from "vue-class-component";

@Options({
  name: "AuthLayoutView",
})
export default class AuthLayoutView extends Vue {

  mounted(){

    document.body.className = "quick-panel-right demo-panel-right offcanvas-right header-fixed header-mobile-fixed subheader-enabled aside-enabled aside-static";

  }

}
