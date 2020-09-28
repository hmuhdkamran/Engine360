import { IMenu } from './model';
import * as icons from './svgs';

export const providedMenu: Array<IMenu> = [
    {
        isVisable: true, name: 'Authentication', icon: icons.defaultIcon, route: '#',
        children: [
            { isVisable: true, name: 'Users', route: 'users' },
            { isVisable: true, name: 'Routes', route: 'routes' },
            { isVisable: true, name: 'Roles', route: 'roles' },
            { isVisable: true, name: 'Role Route Map', route: 'roleroutemap' },
            { isVisable: true, name: 'User Role Map', route: 'userrolemap' },
            { isVisable: true, name: 'Queries', route: 'queries' }
        ]
    },
];