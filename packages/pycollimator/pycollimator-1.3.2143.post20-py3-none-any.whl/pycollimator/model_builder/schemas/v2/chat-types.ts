/* tslint:disable */

export enum FinishReason {
  Stop = 'stop',
  Length = 'length',
  FunctionCall = 'function_call',
  ContentFilter = 'content_filter',
}

export enum ChatMessageRole {
  System = 'system',
  User = 'user',
  Assistant = 'assistant',
  Function = 'function',
}

export interface FunctionCall {
  name: string;
  arguments: string;
}

export interface ChatMessage {
  role: ChatMessageRole;
  content: string;

  originalUserContent?: string;
  automaticMessageContent?: string;

  functionName?: string;
  functionArgs?: string;
  functionResult?: string;
  functionHasError?: boolean;
}

export interface ChatCompleteRequestPayload {
  messages: ChatMessage[];
  temperature: number;
  model: string;
}

export interface ChatCompleteResponsePayload {
  streamUuid: string;
  content?: string;
  finishReason?: FinishReason;
  functionCall?: FunctionCall;
}

export interface Plot {
  id: string;
  value: string; // b64 encoded png
}

// snake_case because it's used in the API
export interface ChatSession {
  session_id: string;
  messages: ChatMessage[];
  plots?: Plot[];
}
