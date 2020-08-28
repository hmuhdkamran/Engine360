
export interface IPayloadMessage {
    text: string;
    title?: string;
    messageTypeId: string;
};

export const PayloadMessageTypes = {
    error: "Error",
    info: "Info",
    failure: "Failure",
    success: "Success",
    warning: "Warning",
}