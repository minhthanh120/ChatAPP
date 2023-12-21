export interface Group {
    id: string | undefined;
    name: string;
    createdBy: string | undefined;
    createdTime: string | undefined;
}
export interface MessageData {
    message: string;
    time?: string;
}