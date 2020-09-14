import { Options, Vue } from "vue-class-component";

import MainView from './main/main.vue';

import MenuView from './header/menu/menu.vue';
import ToolBar from './header/toolbar/toolbar.vue';
import FooterView from './footer/footer.vue';

import { QuickActions, QuickPanel, QuickUser, QuickNotifications } from './panels';

@Options({
  name: "LayoutView",
  components: {
    'main-view': MainView,
    'tool-bar': ToolBar,

    'menu-view': MenuView,

    'quick-notifications': QuickNotifications,
    'quick-actions': QuickActions,
    'quick-panel': QuickPanel,
    'quick-user': QuickUser,

    'footer-view': FooterView
  },
})
export default class LayoutView extends Vue {

  private height: string = "120px;"

  mounted() {
    this.height = `${window.innerHeight}px;`;

    document.body.className = "quick-panel-right demo-panel-right offcanvas-right header-fixed header-mobile-fixed aside-enabled aside-static";
  }
}
