import { Options, Vue } from "vue-class-component";
import { IMenu } from './model';
import { providedMenu } from './pre-menu';

import MenuItem from './menu-item.vue';

@Options({
  name: "MenuView",
  components: {
      'menu-item': MenuItem
  }
})
export default class MenuView extends Vue {

    private menuRepo = providedMenu;

}
