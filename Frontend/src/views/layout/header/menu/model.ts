export interface IMenu {
    name: string;
    route: string;
    icon?: string;
    isVisable: boolean;
    children?: Array<IMenu>;
};