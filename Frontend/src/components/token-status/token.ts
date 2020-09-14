import { Options, Vue } from "vue-class-component";
import { AuthenticationService } from '@/views/services/auth';
import { IUser, IPayloadMessage, PayloadMessageTypes, StoreTypes } from '@/system/models';
import { ICommonState } from '@/system/store/system/state';

@Options({
    name: "TokenStatus",
    props: ['infoTimeout', 'warnTimeout', 'errorTimeout', 'logout']
})
export default class TokenStatus extends Vue {

    private auth: AuthenticationService = null;

    errorTimeout: boolean = (<any>this).errorTimeout;
    infoTimeout: number = (<any>this).infoTimeout;
    logout: boolean = (<any>this).logout;
    warnTimeout: number = (<any>this).warnTimeout;

    private infoHandle: number = null;
    private warnHandle: number = null;
    private errorHandle: number = null;

    private user: IUser = this.$store.state.common.user;

    created() {

        this.auth = new AuthenticationService(this.$store);

        if (this.user.exp)
            this.setHandlers(this.user.exp);

        this.$store.watch(() => this.$store.state.common.user.exp, this.tokenExpiryChanged);
    }

    tokenExpiryChanged(tokenExpiresAt: Date) {
        this.clearHandlers();

        if (tokenExpiresAt)
            this.setHandlers(tokenExpiresAt);
    }

    private clearHandlers() {

        if (this.infoHandle)
            window.clearTimeout(this.infoHandle);

        if (this.warnHandle)
            window.clearTimeout(this.warnHandle);

        if (this.errorHandle)
            window.clearTimeout(this.errorHandle);
    }

    private setHandlers(tokenExpiresAt: Date) {

        if (tokenExpiresAt) {

            let ms = tokenExpiresAt.getTime() - new Date().getTime();
            let seconds = (ms / 1000);

            if (this.infoTimeout && seconds > this.infoTimeout)
                this.infoHandle = window.setTimeout(() => this.info(), ms - this.infoTimeout * 1000);

            if (this.warnTimeout && seconds > this.warnTimeout)
                this.warnHandle = window.setTimeout(() => this.warn(), ms - this.warnTimeout * 1000);

            if (this.errorTimeout)
                this.errorHandle = window.setTimeout(() => this.error(), tokenExpiresAt.getTime() - new Date().getTime());
        }
    }

    private info() {

        let msg: IPayloadMessage = {
            text: 'token expires at ' + this.user.exp.toLocaleString(),
            messageTypeId: PayloadMessageTypes.info
        }

        this.$store.dispatch(StoreTypes.updateStatusBar, msg);
    }

    private warn() {
        let msg: IPayloadMessage = {
            text: 'token expires at ' + this.user.exp.toLocaleString(),
            messageTypeId: PayloadMessageTypes.warning
        }

        this.$store.dispatch(StoreTypes.updateStatusBar, msg);
    }

    private error() {

        let msg: IPayloadMessage = {
            text: 'token expired',
            messageTypeId: PayloadMessageTypes.error
        }

        let logout = this.logout == null ? true : this.logout;

        if (logout)
            this.auth.logout()
                .then(value => this.$store.dispatch(StoreTypes.updateUser, value))
                .then(() => this.$store.dispatch(StoreTypes.updateStatusBar, msg))
                .then(() => this.$router.push({ name: 'login' }));
        else
            this.$store.dispatch(StoreTypes.updateStatusBar, msg)
    }

}
