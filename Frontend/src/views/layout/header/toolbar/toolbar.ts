import { Options, Vue } from "vue-class-component";


@Options({
  name: "ToolBar",
})
export default class ToolBar extends Vue {
  private updateSidebar() {
    console.log(`sidebar-collapse: ${document.body.className.indexOf('sidebar-collapse')}`)
    if (document.body.className.indexOf('sidebar-collapse') >= 0) {
      document.body.classList.remove('sidebar-collapse');
    } else {
      document.body.className += ' sidebar-collapse';
    }
  }
}
