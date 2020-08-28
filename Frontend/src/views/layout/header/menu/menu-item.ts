import { Options, Vue } from "vue-class-component";
import { IMenu } from './model';

@Options({
  name: "MenuItem",
  props: { userMenu: Object }
})
export default class MenuItem extends Vue {

    private userMenu: IMenu = (<any>this).userMenu;
    private isOpened: boolean = false;
    
    get hasChildrens() {
        return this.userMenu.children && this.userMenu.isVisable;
    }

}
