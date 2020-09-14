

import { Options, Vue } from "vue-class-component";
import { UseAxios, TokenHelper } from '@/system/config';
import { useRouter } from 'vue-router';
import { RootStoreTypes } from '@/system/models/store/types';
import { RouteNames } from '@/router/helper';
import { Loader, TokenStatus } from "@/components"
import Store from '@/system/store/app';

@Options({
  name: "ApplicationView",
  components: { "loader": Loader, "token-status": TokenStatus },
  computed: {
    isLoading: () => Store.state.common.isLoading
  }
})
export default class ApplicationView extends Vue {

  created() {
    let router = useRouter();
    UseAxios();

    let token = TokenHelper.getAccessToken();

    let resumeExternalLogin = () => {
      if (location.hash) {

        let hash = location.hash.substring(1);

        if (hash.indexOf("error") != -1 || hash.indexOf("state") != -1 || hash.indexOf("token") != -1) {
          router.push({ name: RouteNames.login, query: { hash: hash } });
        }
      }
    }

    this.$store.dispatch(RootStoreTypes.common.updateUser, token)
      .then(() => this.$store.dispatch(RootStoreTypes.common.loadingState, false))
      .then(() => resumeExternalLogin());
  }
}
