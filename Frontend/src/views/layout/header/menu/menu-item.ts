import { Options, Vue } from "vue-class-component";
import { IMenu } from './model';

@Options({
  name: "MenuItem",
  props: { userMenu: Object, index: String }
})
export default class MenuItem extends Vue {

    private userMenu: IMenu = (<any>this).userMenu;
    private index: String = (<any>this).index;

    private isOpened: boolean = false;

    currentIndex(indexed: string) {
      return `${this.index}.${indexed}`;
    }
    
    get hasChildrens() {
        return this.userMenu.children && this.userMenu.isVisable;
    }

}
