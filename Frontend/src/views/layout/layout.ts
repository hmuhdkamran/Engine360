import { Options, Vue } from "vue-class-component";

import MainView from './main/main.vue';

import MenuView from './header/menu/menu.vue';
import ToolBar from './header/toolbar/toolbar.vue';
import FooterView from './footer/footer.vue';

@Options({
  name: "LayoutView",
  components: {
    'main-view': MainView,
    'tool-bar': ToolBar,

    'menu-view': MenuView,
    
    'footer-view': FooterView
  },
})
export default class LayoutView extends Vue {
  private height: string = "120px;"
  mounted() {
    this.height = `${window.innerHeight}px;`;

    document.body.className = "sidebar-mini layout-fixed control-sidebar-slide-open accent-navy";
  }
}
